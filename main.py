from src.chunking import text_splitter
from src.data_loader import dataload

#document path
PATH = r"C:\Users\panka\OneDrive\Desktop\rag_pdf.pdf"


def main():
    docs = dataload(PATH)
    texts = text_splitter(docs)
    return texts   

if __name__ == "__main__":
    main()
