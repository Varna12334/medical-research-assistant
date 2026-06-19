# Multi-Agent Medical Research Assistant

An intelligent research support system using Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and Multi-Agent AI (CrewAI) to automate medical literature analysis.

## 🚀 Features
- **Multi-Agent Collaboration:** Specialized agents for search, validation, summarization, and reporting.
- **Evidence-Based:** Uses RAG with ChromaDB to retrieve authoritative medical data.
- **Source Credibility:** Automated validation of retrieved literature.
- **Structured Outputs:** Generates ready-to-use research reports with citations.

## 🛠 Tech Stack
- **Framework:** CrewAI, LangChain
- **LLM:** Llama 3
- **Vector Store:** ChromaDB
- **Frontend:** Streamlit

## 📦 Installation
1. Clone the repository:
   `git clone https://github.com/Varna12334/medical-research-assistant.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Set your environment variables in a `.env` file:
   `OPENAI_API_KEY=your_key_here`
4. Run the application:
   `streamlit run main.py`
