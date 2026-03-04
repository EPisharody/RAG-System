# 🔍 Python RAG System

## Overview
A portfolio project that allows users to input queries and generate a response using retrieval augmented generation (RAG). The system includes data ingestion pipeline where data is loaded, cleaned, and split into smaller chunks, a module dedicated to creating embeddings and storing chunks into a vector database, and a module for the LLM.

## Tech Stack
- Python 3.11
- LangChain
- ChromaDB
- Ollama (Mistral 7B chat model)
- HuggingFace embeddings

## How to Run

### Steps
1. Clone repository
   ` git clone https://github.com/EPisharody/RAG-System.git `
2. Navigate to project root directory
3. Run the project using the command `python3 main.py <your_query>`. Optional `--clear` flag to clear the database.

## Future Improvements
- Add unit tests
- Add support for markdown files
- Add UI for more user-friendly experience

## Skills Learned
This project was built as part of a portfolio to demonstrate understanding of:
- Modular Python application design
- Data cleaning
- RAG pipeline
- Using LLMs
