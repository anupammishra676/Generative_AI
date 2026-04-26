from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions=32)

documents = [
    "delhi is capital of india",
    "Patna is capital of bihar",
    "I am anupam mishra"
]

#embed_documents is used to generate embedding for documents
result = embedding.embed_documents(documents)

print(result)