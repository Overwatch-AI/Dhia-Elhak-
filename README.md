# Retrieval-Augmented Generation (RAG) System for Boeing 737 Service Documentation

### **Project Tagline:**  
*A Contextual AI Solution for Accelerating Knowledge Retrieval and Decision Support for pilots.*

---

## 1. Introduction and Project Mandate

This repository presents a specialized **Retrieval-Augmented Generation (RAG)** system designed to interface with the extensive service and maintenance documentation for the **Boeing 737 platform**.  
The primary objective of this project is to overcome the inherent limitations of standard Large Language Models (LLMs) by grounding their generative capabilities in a proprietary, domain-specific knowledge corpus.

By ensuring that responses are **verifiable**, **up-to-date**, and **strictly derived from authorized technical manuals**, this RAG system significantly improves information accessibility, minimizes the risk of LLM hallucination, and elevates the efficiency and accuracy of maintenance procedures and technical troubleshooting.

---

## 2. Architecture: The RAG Pipeline

The system architecture is structured as a robust, **three-stage pipeline** (Indexing, Retrieval, and Generation) to ensure maximum contextual relevance and factual accuracy.

Project Structure: 

```bash
Rag-B737-Service-Repo/
├─ new_data/ ## run Preprocessing.py to generate it
│  ├─ page_images/              # images of the pages (page_*.png)
│  ├─ manual_text.index         # index of the embedded text chunks
│  ├─ manual_diagram.index      # index of the embedded context of the pages 
│  ├─ manual.json               # mapping between different components : chunk_text, page_number, diagram_text and path to the relative page image  
├─
├─ RAG_SERVICES/  
│  ├─ model_wrapper.py          # functions to : embed the query, load images of relevant pages, construct the prompt and pass it to the model API   
│  ├─ vector_store.py           # DualFAISSVectorStore class for reading indexes and running cosine similarity search over them 
├─ Preprocessing.py             # generates the new_data/ folder 
├─ main.py                      # server -> python main.py
├─ .env.example                 # names and examples of all environment variables needed to run the server
├─ requirements.txt             # all dependencies
├─ app.py                       # simple streamlit interface
```

---

### **2.1. The Indexing Phase (Corpus Preparation)**
**2.1.1. Text based indexing**
- **Document Ingestion:**  
  Boeing B737 Manual is loaded via specialized Document Loaders (PyMuPDF), preserving metadata crucial for source attribution.

- **Chunking Strategy:**  
  Documents are segmented into fixed-size chunks with configured overlap. This process is optimized for balancing retrieval granularity (to minimize noise) and context preservation (to maintain relational data within the text).

- **Vectorization (Embedding):**  
  Each text chunk is transformed into a high-dimensional numerical vector (embedding) using a state-of-the-art Embedding Model  (google's text-embedding-004). This vector space represents the semantic meaning of the text.

- **Vector Store Persistence:**  
  The resulting vectors are stored in a performant **Vector Database** (e.g., Chroma, Pinecone, or similar) alongside their original text and metadata, enabling rapid similarity searches.

**2.1.2. Diagram/Tables context indexing**

the semantic context of diagrams,images and tables in the manual is lost while working only on text extraction and embedding, so a more sophisticated method is needed to preserve the context existing in diagrams,images and tables, for that we decided to use gemini **gemini-2.5-flash-preview-09-2025** to extract context from each page containing diagrams,images ot tables, than for each embedded text chunk we correspond to it the relevant context embedding of the page it belongs to

here is an snippet from the preprocessing script showcasing the context extraction prompt passed to the model: 

```python
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
```

**2.1.3. Format of the final mapping between text and context embeddings**

```python
{
    "page_number": page_num,
    "chunk_index": i,
    "text": chunk_text,
    "image_path": img_path,
    "diagram_text": diagram_text, --> context embedding
}

```



---

### **2.2. The Retrieval Phase (Contextual Search)**

- **Query Vectorization:**  
  A user's natural language query is similarly converted into an embedding vector.

- **Cosine Similarity search:**  
  The query vector is used to perform a high-speed similarity search within the Vector Database. This identifies the *k* most semantically similar document chunks.

  **NB:** the search is done simultaneously over **text** and **diagram_text**, a final similarity score is than calculated based on the two previous scores : 

  ```python
  text_scores, text_idx = self.text_index.search(query, k)
  diagram_scores, diagram_idx = self.diagram_index.search(query, k)
  
  # Merge results from both indices
        for i in range(k):
            for idx, s, kind in [(text_idx[0][i], text_scores[0][i], "text"),
                                 (diagram_idx[0][i], diagram_scores[0][i], "diagram")]:
                if idx == -1 or idx not in self.mapping:  # skip invalid indices
                    continue
                if idx not in results:  # initialize result entry
                    results[idx] = {"score": 0, "text_score": 0, "diagram_score": 0, **self.mapping[idx]}
                # Assign individual scores
                if kind == "text":
                    results[idx]["text_score"] = float(s)
                else:
                    results[idx]["diagram_score"] = float(s)
  ```
- **Context Construction:**  
  The retrieved chunks—the “grounding context”—are extracted and bundled. This set of verifiable knowledge is then passed to the LLM.
  We exactly pass the page number, text and the image of the full page (so the LLM will be concient of the visual context) 

### **2.3. The Generation Phase (Grounded Response)**

- **Augmented Prompting:**  
  The retrieved context is integrated into a refined, domain-specific prompt template, which also includes the original user query and strict instructions to the LLM.

- **Large Language Model (LLM) Invocation:**  
  The LLM receives the augmented prompt and is constrained to synthesize a response only using the provided grounding context.

- **Source Attribution:**  
  The final generated response is accompanied by metadata from the retrieved chunks, ensuring complete traceability and facilitating auditability of the information source within the B737 documentation.

---
  code snippet : Prompt construction 

  ```python
  def _create_multimodal_prompt(question: str, chunks: List[Dict[str, Any]]) -> List[Any]:
    """
    Constructs the complex multimodal prompt for the Gemini API.
    This includes system instructions, the query, and all retrieved text/images.
    """

    # 1. System Instruction
    page_numbers = sorted(list(set([c["page_number"] for c in chunks])))
    system_instruction = f"""
    You are an expert aviation assistant for a Boeing 737.
    Your task is to answer the user's question based *only* on the provided context.
    The context consists of text and full-page images from the technical manual.
    The page numbers for the provided context are: {page_numbers}.
    
    CRITICAL RULES:
    1.  Base your answer *exclusively* on the text and images provided.
    2.  Do not add any information not present in the context.
    3.  If the answer is not in the context, state that you cannot find the information in the provided documents, otherwise Do NOT make comments about the context provided.  
    4.  Analyze both the text and the images (diagrams, tables, schemas) to formulate your answer.
    5.  Provide a clear, concise, and accurate answer to the user's question.
    6.  Do NOT repeat the page numbers in your final answer. The system will cite them. Just provide the answer. 
    [IMPORTANT OUTPUT FORMAT]
    At the end of your answer, on a new line, include the list of relevant pages in the following exact format:
    Relevant Pages: [page_numbers]

    For example:
    Relevant Pages: [12]
    or
    Relevant Pages: [41, 42] 
    """

    # 2. Construct the prompt parts list
    prompt_parts = [system_instruction, f'USER QUESTION: "{question}"\n\n--- PROVIDED CONTEXT ---']

    # 3. Add all retrieved chunks (text and images)
    # We sort by page number to give the model a logical flow.
    sorted_chunks = sorted(chunks, key=lambda x: x["page_number"])

    for chunk in sorted_chunks:
        page_num = chunk["page_number"]
        text = chunk["text"]
        image_path = chunk["image_path"]

        # Add the text context
        prompt_parts.append(f"\n--- START: Context from Page {page_num} (Text) ---")
        prompt_parts.append(text)
        prompt_parts.append(f"--- END: Context from Page {page_num} (Text) ---")

        # Add the image context
        base64_data, mime_type = _load_image_as_base64(image_path)
        if base64_data:
            prompt_parts.append(f"\n--- START: Context from Page {page_num} (Image) ---")
            prompt_parts.append(
                {
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": base64_data,
                    }
                }
            )
            prompt_parts.append(f"--- END: Context from Page {page_num} (Image) ---")
        else:
            prompt_parts.append(f"[Image for page {page_num} could not be loaded]")

    return prompt_parts
  ```

---


