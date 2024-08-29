from graph.chains.generation import generation_chain
from graph.graph_state import GraphState
from typing import Any, Dict

def generate(state: GraphState) -> Dict[str, Any]:
    print("---Generate---")

    question = state["question"]
    documents = state["documents"]
    generation = generation_chain.invoke(
        {
            "question": question,
            "context": documents,
        }
    )

    return {
        "question": question,
        "generation": generation,
    }
