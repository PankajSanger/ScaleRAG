from itertools import islice
from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()

@traceable
def dataload(path):
    loader = PyMuPDFLoader(file_path=path,
                           extract_images=True,
                           extract_tables='markdown')

    #importing only first 10 pages from 462 page pdf
    docs = list(islice(loader.lazy_load(), 10))

    return docs
