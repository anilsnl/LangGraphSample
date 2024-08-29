from typing import List, TypedDict

class GraphState(TypedDict):
    """
    The state of the graph
    Arguments:
        question: str
            The user's question

        genaration: str
            The LLM generated result

        web_search: bool
            The data source to route the query to web

        documents: List[str]
            The retrieved documents

    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]