from src.data_loader import dataload

#document path
PATH = r"C:\Users\panka\OneDrive\Desktop\ScaleRAG\data\rag_pdf.pdf"

def main():
    docs = dataload(PATH)
    return docs    

if __name__ == "__main__":
    main()
