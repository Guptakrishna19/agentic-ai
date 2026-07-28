# Week 5 Review — Retrieval-Augmented Generation (RAG)

## Overview

During Week 5, I learned how Retrieval-Augmented Generation (RAG) can be used to build AI applications that answer questions using external documents.
A normal Large Language Model relies mainly on the knowledge available from its training. RAG allows an application to provide additional external knowledge to the LLM before generating an answer.
The basic RAG pipeline is:

Document → Load → Chunk → Embed → Store → Retrieve → Generate Answer

## 1. Document Loading

The first step of a RAG pipeline is loading documents.

Documents can come from different sources such as:

* TXT files
* PDF files
* Web pages
* Databases

Document loaders convert these sources into a format that can be processed by the RAG pipeline.

---

## 2. Document Chunking

Large documents are divided into smaller sections called chunks.
Chunking is important because embedding and retrieving an entire large document is inefficient.
Smaller chunks allow the retriever to find specific sections that are most relevant to a user's question.
A chunk overlap can also be used so that important context is not lost between neighboring chunks.

## 3. Embeddings

An embedding model converts text into numerical vectors.
These vectors represent the semantic meaning of the text.
Texts with similar meanings usually have vectors that are closer together in vector space.
For example:

"How can I reset my password?"

and

"I forgot my password."

have similar meanings and should have similar embeddings.

## 4. Vector Database

Document embeddings are stored inside a vector database.
In this project, FAISS was used as the vector store.
The vector database allows the application to perform similarity searches.
When a user asks a question, the application searches for document chunks whose embeddings are most similar to the question.

## 5. Retriever

A retriever is responsible for finding the most relevant document chunks for a user's question.
The process is:

User Question

→ Search Vector Database

→ Find Similar Chunks

→ Return Relevant Context

The retrieved context is then provided to the Large Language Model.

## 6. Retrieval-Augmented Generation

RAG combines retrieval with text generation.
The process is:

User Question

→ Retriever

→ Relevant Document Chunks

→ Context + Question

→ Large Language Model

→ Final Answer

This allows the LLM to answer questions using information from external documents.
RAG can reduce hallucinations because the model receives relevant context before generating its answer.

## 7. Source Citations

Source citations were added to the RAG pipeline.
Each document chunk contains metadata about its original source.
When the retriever finds relevant chunks, the application can extract the source filename from the metadata.
The API returns both the generated answer and its sources.

Example:

{
"answer": "Digital payments allow users to transfer money electronically.",
"sources": [
"fintech_knowledge_base.txt"
]
}

Source citations make RAG systems more transparent because users can identify where the information came from.

## 8. FastAPI Integration

The RAG pipeline was wrapped inside a FastAPI web application.
Two main API endpoints were created.

### POST /upload

The `/upload` endpoint allows users to upload TXT documents.
The uploaded document goes through:
Upload

→ Read Text

→ Chunk Text

→ Generate Embeddings

→ Store in FAISS
After processing, the document becomes searchable.

### POST /ask

The `/ask` endpoint accepts a question.
The question goes through:
Question

→ Retriever

→ Relevant Chunks

→ LLM

→ Answer

The API returns the generated answer along with the source document.

## 9. File Upload Handling

FastAPI's `UploadFile` was used to receive uploaded documents.
The uploaded TXT file is read and saved to the uploads directory.
The document is then passed to the RAG ingestion pipeline.
Only TXT files are accepted in the current implementation.

## 10. Simple Frontend

A simple HTML, CSS, and JavaScript frontend was created.
The interface allows users to:
1. Select a TXT document.
2. Upload the document.
3. Ask questions about the document.
4. View the generated answer.
5. View the source used to generate the answer.

JavaScript's `fetch()` API communicates with the FastAPI backend.

## 11. Complete Application Flow

The final application works as follows:
User uploads TXT
→ FastAPI `/upload`

→ Document Chunking

→ Embedding Generation

→ FAISS Vector Store

Then:

User asks question

→ FastAPI `/ask`

→ Retriever

→ Relevant Document Chunks

→ LLM

→ Generated Answer

→ Source Citation

→ Display on Frontend

## 12. Key Learnings

During Week 5, I learned:

* What Retrieval-Augmented Generation is.
* Why LLMs need external knowledge.
* How to load documents using LangChain.
* How document chunking works.
* What embeddings are and why they are important.
* How vector databases store embeddings.
* How similarity search works.
* What a retriever does.
* How to combine retrieved context with an LLM.
* How to add source citations.
* How to expose a RAG pipeline through FastAPI.
* How to handle file uploads.
* How to connect an HTML frontend with a FastAPI backend.

## Conclusion

Week 5 focused on building a complete Retrieval-Augmented Generation pipeline and turning it into a usable web application.

The final system allows users to upload their own TXT documents and ask questions about the uploaded content.

The RAG pipeline retrieves relevant information from the document and provides it to the LLM before generating an answer.

FastAPI exposes the RAG functionality through web API endpoints, while the HTML frontend provides a simple interface for interacting with the system.

This project demonstrates the basic architecture used in applications such as document question-answering systems, knowledge assistants, Chat-with-PDF applications, research assistants, and enterprise knowledge search tools.
