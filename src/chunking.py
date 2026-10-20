from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()

@traceable
def text_splitter(docs):

    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)

    texts = splitter.split_documents(docs)

    return texts