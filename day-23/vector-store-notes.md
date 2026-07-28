# Vector Store Notes

## What are Embeddings?

Embeddings are numerical representations of text.

An embedding model converts text into a list of numbers called a vector.

Example:

"Python is used for machine learning."

↓

[0.23, -0.45, 0.78, ...]

Texts with similar meanings usually have vectors that are closer to each other.

---

## Simple Analogy

Think of embeddings like coordinates on a map.

On a normal map, similar places may be located close together.

For example:

- Restaurants may be located in one area.
- Hospitals may be located in another area.
- Schools may be located in another area.

Embeddings work similarly, but instead of physical location, they represent meaning.

For example:

"Dog"
"Puppy"
"Pet"

These concepts would be located close together in the embedding space.

But:

"Stock Market"

would likely be much farther away.

Therefore:

Similar meaning = vectors closer together.

---

## What is a Vector?

A vector is simply a list of numbers.

Example:

[0.23, -0.51, 0.82, 0.14]

Embedding models convert text into high-dimensional vectors containing many numbers.

These numbers allow computers to mathematically compare the semantic similarity between texts.

---

## What is a Vector Store?

A vector store stores and searches embeddings efficiently.

Examples include:

- Chroma
- FAISS
- Pinecone

In this task, I used Chroma.

The basic process is:

Document
↓
Split into chunks
↓
Generate embeddings
↓
Store embeddings in Chroma
↓
User query
↓
Generate query embedding
↓
Similarity search
↓
Return most relevant chunks

---

## What is Similarity Search?

Similarity search finds the chunks whose embeddings are closest to the embedding of a user's query.

For example:

Stored chunks:

1. "Python is used for machine learning."
2. "Dogs are common household pets."
3. "Artificial intelligence allows machines to perform intelligent tasks."

Query:

"What programming language is useful for AI?"

The query is converted into an embedding.

The vector store compares this embedding with the stored embeddings and returns the most similar chunks.

---

## What does k=3 mean?

In similarity search:

k=3

means return the top 3 most relevant chunks.

Example:

results = vector_store.similarity_search(
    query,
    k=3
)

This retrieves the three chunks whose meanings are most similar to the query.

---

## Summary

Embeddings convert text into numerical vectors that represent semantic meaning.

A vector store such as Chroma stores and indexes these vectors.

Similarity search converts a user's query into a vector and finds the stored vectors that are closest to it.

This is an important part of RAG because it allows an AI application to retrieve relevant information before generating an answer.