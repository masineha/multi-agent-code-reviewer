# 🤖 Multi-Agent Code Reviewer

An AI-powered **multi-agent Python code review system** built using **LangGraph**, **LangChain**, and **Groq LLMs**.  
It automatically reads, reviews, and summarizes Python files for **style**, **logic**, and **readability** issues — then generates a **comprehensive markdown report**.

---

## 🧠 Overview

This project demonstrates how multiple specialized AI agents can collaborate:
1. **Reader Agent** — Reads `.py` files and summarizes their purpose.  
2. **Style Reviewer** — Checks code style, readability, and PEP8 conventions.  
3. **Logic Reviewer** — Reviews for logical flaws, edge cases, and optimization.  
4. **Aggregator Agent** — Combines all feedback into a clean markdown report.

---

## 🚀 Features

- 🧩 Modular multi-agent design using **LangGraph**
- 💬 LLM-powered reasoning via **Groq (Llama 3.1 8B Instant)**
- 📁 Automated multi-file analysis
- 📝 Markdown report generation
- ⚙️ Easy to extend with new reviewer agents

---

## 🧰 Tech Stack

- Python 3.12+
- [LangChain](https://python.langchain.com/)
- [LangGraph](https://docs.langchain.com/langgraph/)
- [Groq API](https://groq.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Setup Instructions

1️⃣ Clone the repo
```bash
git clone https://github.com/masineha/multi-agent-code-reviewer.git
cd multi-agent-code-reviewer/

2️⃣ Create & activate a virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Add your API key

Create a .env file in the project root with:

GROQ_API_KEY=your_api_key_here

5️⃣ Run the reviewer

Put your Python files inside a folder named sample_code/
Then run:

python main.py

A formatted review will be generated in:

code_review_report.md


