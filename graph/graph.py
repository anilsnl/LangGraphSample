import graph.nodes.node_constants as node_constants
from graph.nodes import retrieve, grade_documents, generate, web_search
from graph.graph_state import GraphStateStore
from graph.chains.router import question_router_chain
from graph.chains.hallucination_grader import hallucination_grader_chain
from graph.chains.answer_grader import answer_grader_chain

from langgraph.graph import END, StateGraph

from dotenv import load_dotenv

from graph.nodes.node_constants import WEB_SEARCH, GENERATE

load_dotenv()

def route_question(state: GraphStateStore) -> str:
    question = state['question']
    router_result = question_router_chain.invoke({'question': question})
    if router_result.data_source == "web":
        return node_constants.WEB_SEARCH
    else:
        return node_constants.RETRIEVE

def decide_to_generate(state: GraphStateStore) -> str:
    if state['web_search']:
        return node_constants.WEB_SEARCH
    else:
        return node_constants.GENERATE

def grade_generation_grounded_in_documents_and_question(state: GraphStateStore) -> str:
    question = state['question']
    generation = state['generation']
    documents = state['documents']

    hallucination_score = hallucination_grader_chain.invoke({ 'generation': generation, 'documents': documents})
    if hallucination_score.binary_score:
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")

        answer_score = answer_grader_chain.invoke({ 'question': question, 'generation': generation})
        if answer_score.binary_score:
            print("---DECISION: GENERATION IS GROUNDED IN QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION IS NOT GROUNDED IN QUESTION, RE-TRY---")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return "not supported"


workflow = StateGraph(GraphStateStore)

workflow.add_node(node_constants.RETRIEVE, retrieve)
workflow.add_node(node_constants.WEB_SEARCH, web_search)
workflow.add_node(node_constants.GENERATE, generate)
workflow.add_node(node_constants.GRADE_DOCUMENTS, grade_documents)

workflow.set_conditional_entry_point(route_question,{
    node_constants.RETRIEVE: node_constants.RETRIEVE,
    node_constants.WEB_SEARCH: node_constants.WEB_SEARCH
})

workflow.add_conditional_edges(
    node_constants.GRADE_DOCUMENTS,
    decide_to_generate,
    {
        node_constants.WEB_SEARCH: node_constants.WEB_SEARCH,
        node_constants.GENERATE: node_constants.GENERATE
    }
)

workflow.add_conditional_edges(
    node_constants.GENERATE,
    grade_generation_grounded_in_documents_and_question,
    {
        "useful": END,
        "not useful": node_constants.GENERATE,
        "not supported": node_constants.WEB_SEARCH
    }
)

workflow.add_edge(node_constants.RETRIEVE, node_constants.GRADE_DOCUMENTS)
workflow.add_edge(WEB_SEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")
