import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=os.getenv("GROQ_API_KEY"))

def logic_reviewer(state):
    """
    Reviews code logic for each Python file from reader_agent output.
    Focuses on potential logical errors, edge cases, and efficiency.
    Returns structured logic feedback for each file.
    """

    files = state.get("files", {})
    if not files:
        raise ValueError("No files found in state for logic reviewer")

    logic_feedback = {}

    for filename, content in files.items():
        prompt = f"""
        You are a senior Python developer and logic auditor.
        Review this code for:
        - Logical errors or flaws in flow
        - Incorrect or unsafe assumptions
        - Missing error handling or edge case coverage
        - Inefficient or redundant logic
        - Suggestions for more optimal or safer implementation

        Respond briefly in markdown with bullet points.

        File: {filename}
        Code:
        {content}
        """

        try:
            response = llm.invoke(prompt)
            logic_feedback[filename] = response.content.strip()
        except Exception as e:
            logic_feedback[filename] = f"Error reviewing file {e}"

    return {
        **state,
        "style_feedback": state.get("style_feedback", {}),
        "files": state.get("files", {}),
        "summaries": state.get("summaries", {}),
        "logic_feedback": logic_feedback}
