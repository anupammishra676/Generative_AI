from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()

documents = [
    Document(page_content="Langchain helps developers build LLM application easily"),
    Document(page_content="Chroma ia a vector database for LLM based search"),
    Document(page_content="Embeddings convert text into high-dimensional vectors"),
    Document(page_content="OpenAI provides powerful embedding models"),
]

embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="my_collection"
)

retriever = vectorstore.as_retriever(search_kwargs={"k" : 2})

query = "What is chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n---Result {i+1}---")
    print(doc.page_content)