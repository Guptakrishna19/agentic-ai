1. RAG is the Retrieval Augmented Generation which helps the LLM to answer questions based on the provided documents   or policies or a dataset.

2. Why RAG?
    - Large language models have limitations such as hallucination, lack of domain-specific knowledge, and inability to access real-time data. RAG addresses these limitations by providing relevant context to the LLM before generating a response.

3.  components of RAG:
    1. Text splitting
    2. Text embedding
    3. Vector store
    4. Retriever
    5. Generator

4. The response that the llm will generate now will be after combining the user query with the relevant data from the stored data in vector db so that the response can be the most accurate possible.

5. It stores the data in the form of embeddings which are the numbers accosiated to the data and are stored in the vector db.

6.  - Allows LLMs to answer questions using private or custom data.
    - Knowledge can be updated without retraining the entire LLM.
    - Provides more relevant domain-specific answers.
