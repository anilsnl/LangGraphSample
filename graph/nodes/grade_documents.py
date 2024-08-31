from graph.chains.retrieval_grader import retrieval_grader_chain
from typing import Any, Dict
from graph.graph_state import GraphStateStore

def grade_documents(state: GraphStateStore) -> Dict[str, Any]:
    print("---Grade Documents---")

    question = state["question"]
    documents = state["documents"]
    filtered_documents = []
    web_search = False

    for doc in documents:
        grade = retrieval_grader_chain.invoke(
            {
                "question": question,
                "documents": doc.page_content,
            }
        )

        if grade.binary_score:
            filtered_documents.append(doc)

    if len(filtered_documents) == 0:
        web_search = True


    return {
        "question": question,
        "documents": filtered_documents,
        "web_search": web_search
    }