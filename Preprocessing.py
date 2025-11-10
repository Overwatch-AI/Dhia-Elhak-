import os
import json
import numpy as np
import faiss
import fitz  # PyMuPDF
from tqdm import tqdm
from dotenv import load_dotenv
from typing import Tuple, List
import time
import google.generativeai as genai

# --- Configuration ---
PDF_FILE_PATH = "Boeing B737 Manual.pdf"
DATA_DIR = "new_modified_data"
IMAGE_DIR = os.path.join(DATA_DIR, "page_images")
TEXT_INDEX_PATH = os.path.join(DATA_DIR, "manual_text.index")
DIAGRAM_INDEX_PATH = os.path.join(DATA_DIR, "manual_diagram.index")
JSON_MAPPING_PATH = os.path.join(DATA_DIR, "manual.json")

IMAGE_DPI = 150
N_CHUNKS_PER_PAGE = 3
OVERLAP_WORDS = 10
TEXT_EMBEDDING_MODEL = "text-embedding-004"
VLM_MODEL = "gemini-2.5-flash-preview-09-2025"


# --- Helper Functions ---
def extract_diagram_context_from_image_bytes(image_bytes: bytes, page_num: int) -> str:
    """Use Gemini VLM to describe the diagram on the page."""
    try:
        model = genai.GenerativeModel(VLM_MODEL)
        prompt = f"""
        Analyze this image (page {page_num}) from a Boeing 737 Operations Manual.
        Instructions:
        1. Describe all visual content on the page equally:
            - Tables
            - Diagrams
            - Charts
            - Technical illustrations
        2. For each element, include:
            - What it represents
            - Any key labels, units, or numerical values
            - Any special notes or warnings
        3. Mention the main condition/context (e.g., dry runway, Flaps 5, pressure altitude)
        4. Make sure all elements are described so that their content can be used for retrieval/search
        5. Do not ignore smaller diagrams or tables; capture their context as well
        6. Maintain a **concise, objective, technical style** (3–6 sentences per element if needed)
        """
        response = model.generate_content([prompt, {"inline_data": {"mime_type": "image/png", "data": image_bytes}}])
        return response.text.strip() if response and response.text else "[No diagram description found]"
    except Exception as e:
        print(f"VLM diagram extraction failed on page {page_num}: {e}")
        return "[Diagram extraction error]"


def get_text_embedding(text: str, model_name: str = TEXT_EMBEDDING_MODEL, retries: int = 5) -> List[float]:
    """Generate embeddings with retry logic."""
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
    """Split text into overlapping chunks."""
    words = text.split()
    total = len(words)
    if total <= 50:
        return [text]

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
    load_dotenv()
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GOOGLE_GEMINI_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)
    doc = fitz.open(PDF_FILE_PATH)
    num_pages = len(doc)
    print(f"Loaded {num_pages} pages.")

    page_data_mapping = {}
    text_embeddings, diagram_embeddings = [], []
    idx = 0

    for page_num in tqdm(range(1, num_pages + 1), desc="Processing pages"):
        page = doc.load_page(page_num - 1)
        text = page.get_text("text").strip() or f"[No text on page {page_num}]"
        pix = page.get_pixmap(dpi=IMAGE_DPI)
        img_bytes = pix.tobytes("png")
        img_path = os.path.join(IMAGE_DIR, f"page_{page_num}.png")
        with open(img_path, "wb") as f:
            f.write(img_bytes)

        diagram_text = extract_diagram_context_from_image_bytes(img_bytes, page_num)
        diagram_emb = get_text_embedding(diagram_text)

        for i, chunk_text in enumerate(split_text_into_chunks(text, N_CHUNKS_PER_PAGE, OVERLAP_WORDS)):
            text_emb = get_text_embedding(chunk_text)
            if text_emb is None:
                continue

            text_embeddings.append(text_emb)
            diagram_embeddings.append(diagram_emb)

            page_data_mapping[idx] = {
                "page_number": page_num,
                "chunk_index": i,
                "text": chunk_text,
                "image_path": img_path,
                "diagram_text": diagram_text,
            }
            idx += 1

    doc.close()

    np_text = np.array(text_embeddings).astype("float32")
    np_diagram = np.array(diagram_embeddings).astype("float32")

    print("Building FAISS indices...")
    faiss.normalize_L2(np_text)
    faiss.normalize_L2(np_diagram)
    text_index = faiss.IndexFlatIP(np_text.shape[1])
    diagram_index = faiss.IndexFlatIP(np_diagram.shape[1])
    text_index.add(np_text)
    diagram_index.add(np_diagram)

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
