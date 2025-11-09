import os
import json
import numpy as np
import faiss
import fitz  
from tqdm import tqdm
from dotenv import load_dotenv
from typing import Tuple
import time

# --- Configuration ---


PDF_FILE_PATH = "Boeing B737 Manual.pdf" 


# Output directories
DATA_DIR = "data"
IMAGE_DIR = os.path.join(DATA_DIR, "page_images")
FAISS_INDEX_PATH = os.path.join(DATA_DIR, "manual.index")
JSON_MAPPING_PATH = os.path.join(DATA_DIR, "manual.json")

# Image settings
IMAGE_DPI = 150 
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2",device="cuda")
# Embedding model
#EMBEDDING_MODEL = "text-embedding-004" # Google's latest embedding model

# --- Helper Functions ---

def get_text_embedding(text: str, retries: int = 5) -> list[float]:
    """Generates embedding for a given text, with exponential backoff."""
    delay = 1
    for i in range(retries):
        try:
            embeddings = embedding_model.encode(text)
            return embeddings
        except Exception as e:
            if "Resource has been exhausted" in str(e) or "429" in str(e):
                print(f"Rate limit hit. Retrying in {delay}s... (Attempt {i+1}/{retries})")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"Error embedding text: {e}")
                return None
    print("Failed to get embedding after all retries.")
    return None

def process_pdf_page(doc, page_num_1_based: int) -> Tuple[str, bytes]:
    """
    Extracts text and renders a PNG image from a single PDF page.
    
    Args:
        doc: The loaded PyMuPDF document object.
        page_num_1_based: The 1-based page number.

    Returns:
        A tuple (text, image_bytes)
    """
    # PyMuPDF is 0-indexed
    page = doc.load_page(page_num_1_based - 1)
    
    # 1. Extract text
    text = page.get_text("text")
    if not text.strip():
        text = f"[BLANK PAGE OR IMAGE-ONLY PAGE {page_num_1_based}]"
        
    # 2. Render image
    pix = page.get_pixmap(dpi=IMAGE_DPI)
    image_bytes = pix.tobytes("png")
    
    return text, image_bytes

# --- Main Preprocessing Script ---

def main():
    print("Starting PDF preprocessing...")
    
    # 1. Load environment variables (for API key)
    load_dotenv()

    # 2. Check for PDF file
    if not os.path.exists(PDF_FILE_PATH):
        print(f"Error: PDF file not found at {PDF_FILE_PATH}")
        print("Please place your PDF file in the root directory.")
        return

    # 3. Create output directories
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # 4. Load PDF
    try:
        doc = fitz.open(PDF_FILE_PATH)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return
        
    num_pages = len(doc)
    print(f"PDF loaded successfully. Found {num_pages} pages.")

    page_data_mapping = {}
    text_vectors = []
    
    # 5. Process each page
    print("Processing pages (extracting text, rendering images, and generating embeddings)...")
    for page_num in tqdm(range(1, num_pages + 1), desc="Processing Pages"):
        
        # Extract text and image
        try:
            text, image_bytes = process_pdf_page(doc, page_num)
        except Exception as e:
            print(f"Warning: Could not process page {page_num}. Skipping. Error: {e}")
            continue
            
        # Save image
        image_filename = f"page_{page_num}.png"
        image_path = os.path.join(IMAGE_DIR, image_filename)
        try:
            with open(image_path, "wb") as f:
                f.write(image_bytes)
        except Exception as e:
            print(f"Warning: Could not save image for page {page_num}. Skipping. Error: {e}")
            continue

        # Get embedding
        embedding = embedding_model.encode(text)
            
        # Store data
        # We use a 0-based index for the list and FAISS
        index_id = page_num - 1
        text_vectors.append(embedding)
        
        page_data_mapping[index_id] = {
            "page_number": page_num,
            "text": text,
            "image_path": image_path
        }

    doc.close()
    
    if not text_vectors:
        print("No vectors were generated. Exiting.")
        return
        
    # 6. Create and save FAISS index
    print("Creating FAISS index...")
    dimension = len(text_vectors[0])
    index = faiss.IndexFlatL2(dimension)  # L2 distance
    
    # FAISS requires a 2D numpy array of type float32
    vectors_np = np.array(text_vectors).astype('float32')
    index.add(vectors_np)
    
    faiss.write_index(index, FAISS_INDEX_PATH)
    print(f"FAISS index saved to {FAISS_INDEX_PATH}")

    # 7. Save the JSON mapping
    with open(JSON_MAPPING_PATH, 'w', encoding='utf-8') as f:
        json.dump(page_data_mapping, f, indent=4)
    print(f"Page data mapping saved to {JSON_MAPPING_PATH}")

    print("\nPreprocessing complete!")
    print(f"Total pages processed: {len(page_data_mapping)}")

if __name__ == "__main__":
    main()