from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class GradeAnswer(BaseModel):
    """
    Binary score for the LLM generated result is related to the user's question.
    """

    binary_score: str = Field(
        ...,
        description="The binary score for the answer task, return 'yes' if the LLM generated result is relevant to the user's question, 'no' otherwise"
    )

llm = ChatOpenAI(temperature="0.5", model="gpt-3.5-turbo")
structured_output = llm.with_structured_output(GradeAnswer)

system_prompt = """
You are an expert to grade the answer task with the LLM generated result and the user's question.
Please provide a binary score for the answer task, return 'yes' if the LLM generated result is relevant to the user's question, 'no' otherwise.
"""

answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "User's question : {question} \n LLM generation : {generation} "),
    ]
)

answer_grader_chain = answer_prompt | structured_output
