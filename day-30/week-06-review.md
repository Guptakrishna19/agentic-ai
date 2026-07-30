# Week 06 Review

**Intern:** Dhruv Lukhi  
**Week:** 06  
**Focus:** LangChain Agents, RAG, LangGraph & CrewAI

---

# Overview

Week 6 focused on building intelligent AI applications using modern agentic AI frameworks. I learned how AI agents use tools, how Retrieval-Augmented Generation (RAG) improves answer accuracy, how LangGraph enables stateful workflow orchestration, and how CrewAI allows multiple AI agents to collaborate on complex tasks.

By the end of the week, I understood when to use LangChain, LangGraph, or CrewAI depending on the application's requirements.

---

# Topics Learned

## LangChain Agents

- AI agents and tool calling
- ReAct reasoning framework
- Creating custom tools using `@tool`
- Integrating multiple tools with an LLM
- Building command-line AI assistants

### Key Takeaways

- Agents decide which tool to use based on the user's query.
- Tool calling enables AI to perform real-world actions such as calculations, web searches, and database queries.
- LangChain simplifies the development of AI-powered assistants.

---

## Retrieval-Augmented Generation (RAG)

- Document loading
- Text chunking strategies
- Embedding models
- Vector databases
- Similarity search
- Retrieval pipelines
- Source citation

### Key Takeaways

- RAG improves factual accuracy by retrieving relevant document chunks before generating responses.
- Embeddings convert text into numerical vectors for semantic search.
- Vector databases store and efficiently retrieve embedded documents.

---

## LangGraph

- Graph-based workflow orchestration
- Nodes
- Edges
- Shared state
- Conditional routing
- Multi-step AI workflows

### Key Takeaways

- LangGraph provides explicit control over AI workflows.
- State is shared across nodes, enabling complex pipelines.
- Conditional edges allow different execution paths depending on user input.
- Suitable for production AI systems.

---

## CrewAI

- Multi-agent collaboration
- Agent roles
- Goals
- Backstories
- Sequential execution
- Parallel execution
- Task delegation

### Key Takeaways

- CrewAI models AI systems as teams of specialists.
- Each agent performs a focused task.
- Multi-agent collaboration produces richer outputs for complex problems.

---

# Projects Completed

### 1. LangChain AI Assistant

- Built an AI assistant using LangChain
- Implemented custom tools
- Practiced tool calling

---

### 2. Document RAG Pipeline

- Loaded documents
- Created embeddings
- Stored vectors
- Retrieved relevant context
- Generated grounded answers

---

### 3. LangGraph Workflow

Designed a workflow with:

- Question classification
- Document retrieval
- Answer generation
- Conditional routing

---

### 4. Startup Business Advisor (CrewAI)

Created multiple collaborating agents:

- Market Researcher
- Competitor Analyst
- Business Strategist
- Financial Advisor
- Pitch Writer

Generated:

- SWOT Analysis
- Competitor Analysis
- Business Model
- Revenue Model
- Elevator Pitch

---

### 5. Multi-Agent Research Assistant

Built a research pipeline where multiple AI agents collaborated to produce structured research summaries.

---

# Framework Comparison

| Feature | LangChain | LangGraph | CrewAI |
|---------|-----------|-----------|---------|
| Primary Focus | Single AI agent | Workflow orchestration | Multi-agent collaboration |
| Ease of Learning | Easy | Moderate | Easy |
| Workflow Control | Medium | Excellent | Moderate |
| State Management | Limited | Excellent | Good |
| Multi-Agent Support | Basic | Possible | Excellent |
| Best For | Chatbots & assistants | Production workflows | Collaborative AI systems |

---

# Skills Gained

- Tool Calling
- ReAct Pattern
- Document Retrieval
- Vector Embeddings
- FAISS
- Chroma
- RAG Pipeline Design
- Graph-Based Workflows
- State Management
- Conditional Routing
- Multi-Agent Collaboration
- Sequential Execution
- Parallel Execution

---

# Challenges Faced

- Understanding how embeddings represent semantic meaning.
- Learning the differences between LangChain, LangGraph, and CrewAI.
- Designing workflow graphs with conditional routing.
- Managing data flow between multiple agents.
- Choosing the right framework for different use cases.

---

# Solutions Learned

- Use LangChain for simple AI assistants.
- Use LangGraph when workflow control and state management are important.
- Use CrewAI when multiple AI agents need to collaborate.
- Use RAG whenever answers should be grounded in external documents.

---

# Biggest Learnings

- Every AI application does not require multiple agents.
- RAG significantly improves factual accuracy.
- LangGraph provides production-level workflow orchestration.
- CrewAI makes multi-agent collaboration straightforward.
- Framework selection depends on the problem rather than popularity.

---

# Which Framework Would I Choose?

For a Document Question Answering (Q&A) application, I would choose **LangGraph**.

Reasons:

- Explicit workflow control
- Persistent state management
- Efficient RAG integration
- Easier debugging
- Lower API costs
- Better scalability
- Reliable production deployment

For collaborative tasks such as market research, business planning, or content creation, I would choose **CrewAI** because specialized agents can divide work and produce comprehensive results.

---

# Overall Reflection

Week 6 greatly expanded my understanding of agentic AI systems. I learned how individual AI agents use tools, how RAG improves knowledge retrieval, how LangGraph orchestrates complex workflows, and how CrewAI enables multiple specialized agents to collaborate effectively.

These concepts have given me a strong foundation for building production-ready AI applications, including intelligent assistants, document question-answering systems, workflow automation, and multi-agent solutions.

I now have a clear understanding of when to use LangChain, LangGraph, and CrewAI based on the complexity and requirements of an AI project.