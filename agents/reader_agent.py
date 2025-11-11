import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=os.getenv("GROQ_API_KEY"))

def reader_agent(state):
    """
    Reads all Python (.py) files from the folder path in the state,
    summarizes each file briefly using an LLM, and returns file contents
    + summaries so other agents can use them.
    """

    folder_path = state.get("path")
    if not folder_path:
        raise ValueError("❌ Missing 'path' in state for reader_agent")

    files = {}
    summaries = {}

    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    files[filename] = content

                    # 🧠 LLM: create a short summary of the file
                    prompt = f"""
                    You are a Python assistant.
                    Summarize this code in one or two sentences — what does it do overall?
                    File name: {filename}
                    Code:
                    {content}
                    """
                    response = llm.invoke(prompt)
                    summaries[filename] = response.content.strip()

                except Exception as e:
                    files[filename] = f"[Error reading file: {e}]"
                    summaries[filename] = "Error reading file."

    return {
         **state,
        "files": files, "summaries": summaries}





