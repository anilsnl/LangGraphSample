from data_seeder.mongo_db_seeder import retriever
from graph.graph_state import GraphState

from typing import Any, Dict


def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---Retrieve---")

    question = state["question"]
    documents = retriever.invoke(question)

    return {
        "question": question,
        "documents": documents,
    }