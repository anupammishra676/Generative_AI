from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions= 300)

documents = [
    "virat kohli is an indian cricketer know for his aggressive batin and leadership",
    "MS dhoni is a former indian captain famous for his calm demeanor and finishing skilss",
    "Sachin Tendulakar, also known as 'god of cricket',  holds many batting records",
    "Rohit Sharma is know for his elegant batting and record-breaking doule centuries",
    "Jaspit bumrah is an indian fast bowler known for unorthodo action and yorkers"
]

query = 'tell me about god of cricket'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]     #Parameters must pass as a 2D array.

index, score = sorted(list(enumerate(scores)),key= lambda x:x[1])[-1]  # Sort it basis on index so that highest score can be come either on 1st or last to achieve the result.

print(query)
print(documents[index])
print("Similarity score is :", score )