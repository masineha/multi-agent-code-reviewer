import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=os.getenv("GROQ_API_KEY"))

def aggregator_agent(state):
    """
    Combines results from style_reviewer and logic_reviewer into
    a final report. It uses the LLM to synthesize the findings
    into a readable markdown summary.
    """

    summaries = state.get("summaries", {})
    style_feedback = state.get("style_feedback", {})
    logic_feedback = state.get("logic_feedback", {})

    if not summaries:
        raise ValueError("No summaries found in state for aggregator_agent")

    report_sections = []

    for filename, summary in summaries.items():
        style = style_feedback.get(filename, "No style feedback available.")
        logic = logic_feedback.get(filename, "No logic feedback available.")

        combined = f"""
        ## 🧾 File: {filename}

        **📝 Summary:**
        {summary}

        **🎨 Style Review:**
        {style}

        **🧠 Logic Review:**
        {logic}

        ---
        """
        report_sections.append(combined)

    # Combine all file reports into one big markdown
    combined_report = "\n".join(report_sections)

    # Optional: have the LLM clean and polish it for readability
    prompt = f"""
    You are a documentation assistant.
    Clean up and format this markdown report for a professional
    developer audience. Keep it concise and structured.

    Report:
    {combined_report}
    """

    response = llm.invoke(prompt)
    final_report = response.content.strip()

    return {"report": final_report}