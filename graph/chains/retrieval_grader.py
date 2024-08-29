from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class RetrievalGrader(BaseModel):
    """
    Binary score for the retrieval task with the user's question and the retrieved documents
    """

    binary_score: str = Field(
        ...,
        description="The binary score for the retrieval task, return 'yes' if the documents are relevant to the question, 'no' otherwise"
    )

llm = ChatOpenAI(temperature="0.5", model="gpt-3.5-turbo")
structured_output = llm.with_structured_output(RetrievalGrader)

system_prompt = """
You are an expert to grade the retrieval task with the user's question and the retrieved documents.
Please provide a binary score for the retrieval task, return 'yes' if the documents are relevant to the question, 'no' otherwise.
"""

retrieval_grader_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Retrieved documents : {retrieved_documents} \n Question : {question} "),
    ]
)

retrieval_grader_chain = retrieval_grader_prompt | structured_output
