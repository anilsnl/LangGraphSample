from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from langchain_openai import ChatOpenAI

class QueryRouter(BaseModel):
    """
    Route user one of the following data sources according to the user's query
    """

    data_source: Literal["vector_store", "web"] = Field(
        ...,
        description= "The data source to route the query to"
    )

llm = ChatOpenAI(temperature="0.5", model="gpt-3.5-turbo")
structured_output = llm.with_structured_output(QueryRouter)

system_prompt = """
You are a expert to route user questions to the right data source which can be either a vector store or the web.
The documents that store the data are in the vector store are about adesso company  documents. For other questions, you can use the web.
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}"),
    ]
)

question_router_chain = route_prompt | structured_output
