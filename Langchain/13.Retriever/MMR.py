from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()

docs = [
    Document(page_content="Langchain helps developers build LLM application easily"),
    Document(page_content="Langchain make it easy to work with LLM"),
    Document(page_content="Chroma ia a vector database for LLM based search"),
    Document(page_content="Embeddings convert text into high-dimensional vectors"),
    Document(page_content="OpenAI provides powerful embedding models"),
    Document(page_content="Langchain supports Chorma, FAISS, Pinecone etc"),
    Document(page_content="MMR helps you get diverse results when doing similarity search")
]

embeddings = OpenAIEmbeddings()

vector_stores = FAISS.from_documents(
    documents=docs,
    embedding=embeddings
)

retriever = vector_stores.as_retriever(
    search_type = "mmr",  #This enable MMR
    search_kwargs={"k" : 3, "lambda_mult" : 0.5}  #k = top results, lambda_mult = relevance-diversity balance (0 - most diversify,  1- least diversify)
)

query = "Where is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n---Result{i+1}---") 
    print(f"Content:\n {doc.page_content}")