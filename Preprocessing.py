import os
import json
import numpy as np
import faiss
import fitz  # PyMuPDF for PDF handling
from tqdm import tqdm
from dotenv import load_dotenv
from typing import Tuple, List
import time
import google.generativeai as genai

# --- Configuration ---
PDF_FILE_PATH = "Boeing B737 Manual.pdf"
DATA_DIR = "new_data"
IMAGE_DIR = os.path.join(DATA_DIR, "page_images")
TEXT_INDEX_PATH = os.path.join(DATA_DIR, "manual_text.index")
DIAGRAM_INDEX_PATH = os.path.join(DATA_DIR, "manual_diagram.index")
JSON_MAPPING_PATH = os.path.join(DATA_DIR, "manual.json")

IMAGE_DPI = 150  # DPI for PDF page rendering
N_CHUNKS_PER_PAGE = 3  # Number of text chunks per page
OVERLAP_WORDS = 10  # Overlap between chunks
TEXT_EMBEDDING_MODEL = "text-embedding-004"
VLM_MODEL = "gemini-2.5-flash-preview-09-2025"


# --- Helper Functions ---
def extract_diagram_context_from_image_bytes(image_bytes: bytes, page_num: int) -> str:
    """Use Gemini VLM to generate a concise description of diagrams/tables on a page."""
    try:
        model = genai.GenerativeModel(VLM_MODEL)
        prompt = f"""
        Analyze this image (page {page_num}) from a Boeing 737 manual. 
        Describe the diagram(s), tables, or technical illustrations concisely:
            - What it represents 
            - The key labeled components 
            - Any units, numerical values, or warnings 
        Output 3–5 sentences maximum, objective and technical
        """
        response = model.generate_content([prompt, {"inline_data": {"mime_type": "image/png", "data": image_bytes}}])
        return response.text.strip() if response and response.text else "[No diagram description found]"
    except Exception as e:
        print(f"VLM diagram extraction failed on page {page_num}: {e}")
        return "[Diagram extraction error]"


def get_text_embedding(text: str, model_name: str = TEXT_EMBEDDING_MODEL, retries: int = 5) -> List[float]:
    """Generate embeddings with retry logic in case of rate limits."""
    delay = 1
    for i in range(retries):
        try:
            result = genai.embed_content(model=model_name, content=text, task_type="RETRIEVAL_DOCUMENT")
            return result["embedding"]
        except Exception as e:
            if "Resource has been exhausted" in str(e) or "429" in str(e):
                print(f"Rate limit hit. Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"Embedding error: {e}")
                return None
    return None


def split_text_into_chunks(text: str, n_chunks: int, overlap_words: int) -> List[str]:
    """Split text into overlapping chunks for embedding."""
    words = text.split()
    total = len(words)
    if total <= 50:
        return [text]  # Short text stays as is

    base_size = total // n_chunks
    overlap = min(overlap_words, base_size // 4) if base_size > 0 else 0
    chunks = []
    for i in range(n_chunks):
        start = max(0, i * base_size - overlap)
        end = (i + 1) * base_size if i < n_chunks - 1 else total
        chunks.append(" ".join(words[start:end]))
    return chunks


# --- Main Processing ---
def build_multimodal_indices():
    print("Starting multimodal preprocessing...")
    
    # Load API key and configure Gemini
    load_dotenv()
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GOOGLE_GEMINI_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)

    # Create directories if they don't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # Open PDF and get total pages
    doc = fitz.open(PDF_FILE_PATH)
    num_pages = len(doc)
    print(f"Loaded {num_pages} pages.")

    # Initialize storage
    page_data_mapping = {}
    text_embeddings, diagram_embeddings = [], []
    idx = 0

    # Process each page
    for page_num in tqdm(range(1, num_pages + 1), desc="Processing pages"):
        page = doc.load_page(page_num - 1)
        text = page.get_text("text").strip() or f"[No text on page {page_num}]"

        # Save page image
        pix = page.get_pixmap(dpi=IMAGE_DPI)
        img_bytes = pix.tobytes("png")
        img_path = os.path.join(IMAGE_DIR, f"page_{page_num}.png")
        with open(img_path, "wb") as f:
            f.write(img_bytes)

        # Extract diagram description and embedding
        diagram_text = extract_diagram_context_from_image_bytes(img_bytes, page_num)
        diagram_emb = get_text_embedding(diagram_text)

        # Split text into chunks and get embeddings
        for i, chunk_text in enumerate(split_text_into_chunks(text, N_CHUNKS_PER_PAGE, OVERLAP_WORDS)):
            text_emb = get_text_embedding(chunk_text)
            if text_emb is None:
                continue

            text_embeddings.append(text_emb)
            diagram_embeddings.append(diagram_emb)

            # Store metadata for each chunk
            page_data_mapping[idx] = {
                "page_number": page_num,
                "chunk_index": i,
                "text": chunk_text,
                "image_path": img_path,
                "diagram_text": diagram_text,
            }
            idx += 1

    doc.close()

    # Convert embeddings to numpy arrays and normalize
    np_text = np.array(text_embeddings).astype("float32")
    np_diagram = np.array(diagram_embeddings).astype("float32")

    print("Building FAISS indices...")
    faiss.normalize_L2(np_text)
    faiss.normalize_L2(np_diagram)

    # Create FAISS indices (Inner Product)
    text_index = faiss.IndexFlatIP(np_text.shape[1])
    diagram_index = faiss.IndexFlatIP(np_diagram.shape[1])
    text_index.add(np_text)
    diagram_index.add(np_diagram)

    # Save indices and mapping
    faiss.write_index(text_index, TEXT_INDEX_PATH)
    faiss.write_index(diagram_index, DIAGRAM_INDEX_PATH)

    with open(JSON_MAPPING_PATH, "w", encoding="utf-8") as f:
        json.dump(page_data_mapping, f, indent=4)

    print("Preprocessing complete.")
    print(f"Saved text index: {TEXT_INDEX_PATH}")
    print(f"Saved diagram index: {DIAGRAM_INDEX_PATH}")
    print(f"Saved mapping JSON: {JSON_MAPPING_PATH}")


if __name__ == "__main__":
    build_multimodal_indices()
