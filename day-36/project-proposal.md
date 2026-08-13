# AI Research Assistant — Project Proposal

GitHub Link: https://github.com/dhruvL21/ResearchLens

## 1. Problem

Researchers and students often spend significant time reading large numbers of documents, extracting relevant information, comparing findings, and preparing structured reports. Traditional document search only retrieves text and does not provide deeper synthesis or automated research workflows.

## 2. Solution

The **AI Research Assistant** is an AI-powered research platform where users can upload research papers, PDFs, reports, and other documents, ask questions about their content, and generate structured research reports.

The system combines **RAG (Retrieval-Augmented Generation)** with a **multi-agent architecture**. Specialized AI agents handle different stages of research such as document retrieval, analysis, fact checking, summarization, and report generation.

## 3. Core Features

* Upload and process PDF/text documents
* Automatic document chunking and embedding generation
* Semantic search over uploaded documents
* RAG-based question answering with source references
* Multi-agent research workflow
* Researcher/analyst agent for extracting key findings
* Fact-checking agent for validating claims against available sources
* Summarizer agent for condensing research
* Report-generation agent for producing structured reports
* Conversation history
* Downloadable research reports
* Basic authentication and user-specific document storage

## 4. Proposed Tech Stack

**Frontend**

* Next.js
* React
* TypeScript
* CSS/Tailwind CSS
* Recharts where analytics are required

**Backend**

* Python
* FastAPI
* LangChain / LangGraph
* Pydantic

**AI**

* OpenAI API
* Embeddings
* RAG
* Multi-agent orchestration

**Database / Storage**

* PostgreSQL or MongoDB
* Vector database: Chroma/FAISS initially
* Object storage for uploaded documents

**DevOps**

* Docker
* GitHub
* GitHub Actions
* Environment variables and structured logging

## 5. Timeline

### Day 36 — Planning & Setup

* Finalize architecture
* Create GitHub repository
* Set up `/backend`, `/frontend`, and `/docs`
* Configure environment variables
* Create initial documentation

### Day 37 — Document Processing & RAG

* Implement document upload
* Extract document text
* Chunk documents
* Generate embeddings
* Store vectors
* Build retrieval pipeline

### Day 38 — Question Answering

* Build FastAPI endpoints
* Connect retriever with LLM
* Implement source-aware answers
* Add validation and error handling
* Test RAG accuracy

### Day 39 — Multi-Agent Research Workflow

* Build LangGraph workflow
* Add research/analysis agent
* Add fact-checking agent
* Add summarization agent
* Add report-generation agent

### Day 40 — Frontend & Integration

* Build research dashboard
* Connect frontend to backend
* Display sources and generated answers
* Add report generation UI
* Test complete end-to-end workflow

## Expected Outcome

By the end of Day 40, the project should have a working AI research platform capable of accepting documents, answering questions using RAG, orchestrating multiple specialized AI agents, and generating structured research reports.
