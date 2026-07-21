# Week 04 Review — Large Language Models and AI Agents

## 1. Large Language Models (LLMs)

A Large Language Model (LLM) is an AI model trained on large amounts of text and code. It can understand natural language and generate human-like responses.

LLMs can perform tasks such as:

- Answering questions
- Text generation
- Summarization
- Translation
- Information extraction
- Code generation
- Classification

Examples of LLMs include GPT models, Gemini, Claude, and Llama.

Basic flow:

User Input → Prompt → LLM → Response

## 2. Prompt Engineering

Prompt engineering is the process of designing clear and structured instructions for an LLM to produce better responses.

A good prompt usually contains:

- Role
- Task
- Context
- Constraints
- Expected output format

Example:

"You are an expert Python teacher. Explain Python dictionaries to a beginner with one simple example."

### System Prompt

A system prompt defines how the AI should behave.

Example:

"You are a helpful programming assistant. Explain concepts in simple language."

### User Prompt

A user prompt contains the actual request made by the user.

Example:

"Explain Python inheritance."

### Prompt Template

A prompt template is a reusable prompt structure containing variables.

Example:

"Explain {topic} to a {level} student."

The same template can be reused with different values.

---

## 3. LangChain

LangChain is a framework used to build applications powered by Large Language Models.

It provides components for working with:

- LLMs
- Prompt templates
- Chains
- Tools
- Agents
- Retrieval
- Conversation workflows

LangChain helps developers connect LLMs with application logic, databases, APIs, and external tools.


## 4. LangChain Chains

A chain connects multiple components together in a predefined sequence.

Example:

Input → Prompt → LLM → Output Parser → Response

Using LangChain Expression Language (LCEL):

prompt | model | parser

Chains are useful when the workflow is already known and predictable.

For example:

User Text → Summarize → Generate Response

## 5. Tools

Tools are functions or external capabilities that an AI agent can use.

Examples include:

- Calculator
- Search
- Weather API
- Database query
- Email sender
- Inventory lookup
- Custom Python functions

A tool allows an LLM-powered application to interact with systems outside the language model.

## 6. AI Agents

An AI agent is a system where an LLM can decide which actions or tools should be used to complete a task.

Basic architecture:

LLM + Tools + Decision Loop = Agent

The agent receives a request, determines what action is required, selects an appropriate tool, observes the result, and generates a final response.

Agent flow:

User Request
↓
Agent
↓
LLM decides what to do
↓
Tool Selection
↓
Tool Execution
↓
Observe Result
↓
Final Response

## 7. Chains vs Agents

### Chain

A chain follows a predefined workflow.

Example:

Input → Prompt → LLM → Output

The developer decides the sequence of operations.

### Agent

An agent dynamically decides which actions and tools are required.

Example:

User Request
↓
Agent
├── Calculator
├── Search Tool
├── Database Tool
└── API Tool
↓
Final Response

Chains are more predictable, while agents are more flexible for dynamic tasks.

## 8. CLI Assistant with an LLM Backend

A Command-Line Interface (CLI) allows users to interact with an AI assistant directly through the terminal.

Basic architecture:

User
↓
Terminal / CLI
↓
LangChain Agent
↓
LLM
↓
Tools
↓
Response
↓
Terminal

The CLI continuously accepts user input until the user enters an exit command.

Example:

You: What is 25 * 8?

Assistant: 200

The agent can choose a calculator tool to perform the calculation and return the result.

---

## 9. Conversation History

Conversation history allows an AI assistant to maintain context between messages.

Example:

User: My name is Dhruv.

Assistant: Nice to meet you, Dhruv.

User: What is my name?

Assistant: Your name is Dhruv.

Previous user and assistant messages are stored and passed back to the LLM with new requests.

In the CLI assistant, only the last 5 messages are retained.

This prevents the conversation history from growing indefinitely while still providing recent context.

---

## 10. Five Real-World Applications of AI Agents

### 1. Customer Support Agents

AI agents can answer customer questions, search knowledge bases, check order information, create support tickets, and escalate complex problems to human employees.

### 2. E-Commerce and Inventory Agents

AI agents can monitor inventory, identify low-stock products, analyze sales data, recommend restocking quantities, and provide business insights.

### 3. Travel Planning Agents

Travel agents can search destinations, compare travel options, create itineraries, estimate budgets, and personalize recommendations based on user preferences.

### 4. Software Development Agents

Coding agents can analyze codebases, generate code, identify bugs, run development tools, assist with testing, and help developers complete programming tasks.

### 5. Research Agents

Research agents can search multiple information sources, collect relevant information, compare findings, summarize documents, and generate structured research reports.


## 11. Key Learnings from Week 04

During Week 04, I learned:

1. How Large Language Models process prompts and generate responses.
2. How prompt engineering improves the quality and consistency of LLM outputs.
3. How LangChain connects prompts, LLMs, parsers, tools, and other components.
4. How chains create predefined LLM workflows.
5. How tools give AI systems access to external functionality.
6. How AI agents dynamically select tools to complete tasks.
7. How to build a CLI application connected to a LangChain agent.
8. How conversation history allows an assistant to remember recent context.

## Conclusion

Week 04 introduced the fundamentals of building AI-powered applications using Large Language Models and LangChain.

The progression was:

LLMs → Prompt Engineering → LangChain → Chains → Tools → Agents → CLI AI Assistant

By combining an LLM with tools, agents, and conversation history, we can build AI applications that not only generate text but can also make decisions, perform actions, access external data, and maintain conversational context.