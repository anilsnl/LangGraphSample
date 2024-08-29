from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class GradeHallucinations(BaseModel):
    """
    Binary score for the LLM generated result is related to the retrieved documents
    thus grading the hallucination task
    """

    binary_score: str = Field(
        ...,
        description="The binary score for the retrieval task, return 'yes' if the documents are relevant to the LLM generated result, 'no' otherwise"
    )

llm = ChatOpenAI(temperature="0.5", model="gpt-3.5-turbo")
structured_output = llm.with_structured_output(RetrievalGrader)

system_prompt = """
You are an expert to grade the retrieval task with the LLM generated result and the retrieved documents.
Please provide a binary score for the retrieval task, return 'yes' if the documents are relevant to the LLM generated result, 'no' otherwise.
"""

hallucination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Retrieved documents : {documents} \n LLM generation : {generation} "),
    ]
)

hallucination_grader_chain = hallucination_prompt | structured_output
