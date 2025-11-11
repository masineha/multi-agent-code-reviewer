import os
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph
from agents.reader_agent import reader_agent
from agents.style_reviewer import style_reviewer
from agents.logic_reviewer import logic_reviewer
from agents.aggregator import aggregator_agent

def build_graph():
    # Use StateGraph with an initial state schema (Python dict)
    graph=StateGraph(dict)

    #add nodes
    graph.add_node("reader",reader_agent)
    graph.add_node("style",style_reviewer)
    graph.add_node("logic",logic_reviewer)
    graph.add_node("aggregator",aggregator_agent)

    #add edges
    graph.add_edge("reader","style")
    graph.add_edge("style","logic")
    #graph.add_edge("style","aggregator")
    graph.add_edge("logic","aggregator")

    #set start and finish
    graph.set_entry_point("reader")
    graph.set_finish_point("aggregator")

    return graph

if __name__ == "__main__":
    folder_path="./sample_code"
    graph=build_graph()
    app=graph.compile()
    result=app.invoke({"path":folder_path})
    
    print("Review complete! Final report:\n")
    print(result["report"])

    with open("code_review_report.md","w") as f:
        f.write(result["report"])
    print("\n Report saved as 'code_reviewer_report.md'")