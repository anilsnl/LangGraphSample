from data_seeder.mongo_db_seeder import retriever
from graph.graph_state import GraphStateStore

from typing import Any, Dict


def retrieve(state: GraphStateStore) -> Dict[str, Any]:
    print("---Retrieve---")

    question = state["question"]
    documents = retriever.invoke(question)

    return {
        "question": question,
        "documents": documents,
    }