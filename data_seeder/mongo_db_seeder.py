import os

from dotenv import load_dotenv
from langchain_openai import  OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders.mongodb import MongodbLoader

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

chrome_collection = Chroma(
    persist_directory=os.getenv('CHROMA_PERSIST_DIRECTORY'),
    collection_name="confluence",
    embedding_function=embeddings,
)

def load_confluence_data():
    connection_string = os.getenv('MONGO_DB_CONNECTION_STRING')
    loader = MongodbLoader(
        connection_string=connection_string,
        db_name="confluence",
        collection_name="pages",
        field_names=["title", "body_flet"],
        filter_criteria={},
    )

    print("Loading data from Confluence")
    documents = loader.load()
    print(f"Loaded {len(documents)} documents from Confluence")
    chrome_collection.reset_collection()
    print("Reset Chroma collection")
    chrome_collection.add_documents(documents)
    print("Added documents to Chroma collection")


retriever = chrome_collection.as_retriever()

if __name__ == '__main__':
    load_confluence_data()
    print('Data loaded successfully!')