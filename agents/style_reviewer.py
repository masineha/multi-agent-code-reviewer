import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=os.getenv("GROQ_API_KEY"))

def style_reviewer(state):
    """
    Reviews code style for each Python file from reader_agent output.
    Focuses on readability, comments, naming conventions, indentation, etc.
    Returns structured style feedback for each file.
    """
    files=state.get("files",{})
    if not files:
        raise ValueError("No files found in state for style reviewer")
    
    style_feedback={}

    for filename, content in files.items():
        prompt=f"""
        You are a senior python reviewer.
        Check this code for:
        - PEP8 style issues (indentation, spacing)
        - Readability and naming conventions
        - Comments and documentation clarity
        - Consistency of variable and function naming

        Respond briefly in markdown with bullet points.

        File: {filename}
        Code:
        {content}
        """

        try:
            response=llm.invoke(prompt)
            style_feedback[filename]=response.content.strip()
        except Exception as e:
            style_feedback[filename]=f"Error reviewing file {e}"
    
    return {
    **state,
    "style_feedback": style_feedback,
    "files": state.get("files", {}),
    "summaries": state.get("summaries", {})
}







