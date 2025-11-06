from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import os
import re
import shutil

def load_listings(file_path="listings.txt"):
    with open(file_path) as f:
        text = f.read()

    raw_listings = re.split(r'\n(?=\d+\.\sNeighborhood:)', text)

    documents = [Document(page_content=l.strip()) for l in raw_listings if l.strip()]
    return documents

def create_vector_db(listings, persist_directory="./chroma_db"):
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("BASE_URL")
    )

    db = Chroma.from_documents(listings, embeddings, persist_directory=persist_directory)
    db.persist()
    return db
