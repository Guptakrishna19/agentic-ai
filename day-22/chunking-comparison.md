# Chunking Strategy Comparison

## Documents Used

Three sample text documents were used:

1. Artificial Intelligence
2. Machine Learning
3. Generative AI

Total documents loaded: 3

---

## Strategy 1: CharacterTextSplitter

### Configuration

- Chunk size: 500 characters
- Chunk overlap: 50 characters

### Chunk Count

7

### First Chunk

```text
Artificial Intelligence

Artificial Intelligence, commonly known as AI, is a branch of computer science focused on creating systems that can perform tasks that normally require human intelligence. These tasks include understanding language, recognizing images, solving problems, making decisions, and learning from experience.

AI systems are used in many areas of everyday life. Virtual assistants use AI to understand voice commands, recommendation systems suggest movies and products, and navigati
```

---

## Strategy 2: RecursiveCharacterTextSplitter

### Configuration

- Chunk size: 500 characters
- Chunk overlap: 50 characters

### Chunk Count

9

### First Chunk

```text
Artificial Intelligence

Artificial Intelligence, commonly known as AI, is a branch of computer science focused on creating systems that can perform tasks that normally require human intelligence. These tasks include understanding language, recognizing images, solving problems, making decisions, and learning from experience.
```
