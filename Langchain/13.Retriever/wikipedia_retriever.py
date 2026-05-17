from langchain_community.retrievers import WikipediaRetriever
from dotenv import load_dotenv

load_dotenv()

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "India Pakistan relations"

docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n---Result{i+1}---")
    print(f"Content:\n {doc.page_content}")