from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()

doc1 = Document(
    page_content="virat kohli is an indian cricketer know for his aggressive batin and leadership",
    metadata={"team" : "RCB"}
)
doc2 = Document(
    page_content="MS dhoni is a former indian captain famous for his calm demeanor and finishing skils",
    metadata={"team" : "CSK"}
)
doc3 = Document(
    page_content="Sachin Tendulakar, also known as 'god of cricket',  holds many batting records",
    metadata={"team" : "ICT"}
)
doc4 = Document(
    page_content="Rohit Sharma is know for his elegant batting and record-breaking doule centuries",
    metadata={"team" : "MI"}
)

docs = [doc1,doc2,doc3,doc4]

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

#vector_store.add_documents(docs) --- One time activity



vector_store.similarity_search(
    query = 'Who is god of cricket',
    k=2  #This indicates that how many top similar result we need 
)

vector_store.similarity_search_with_score(
    query='who was the former indian captain',
    k=2
)

print(vector_store.similarity_search_with_score(
    query="",
    filter={"team": "RCB"}
))

update_doc1 = Document(
    page_content= "Virat kohli, is the superstar of indian cricket",
    metadata={"team" : "RCB"}
)

vector_store.update_document(document_id='b7663137-e007-43fe-b2aa-1dfe989d46a2', document=update_doc1)

vector_store.delete(ids=['b7663137-e007-43fe-b2aa-1dfe989d46a2'])

print(vector_store.get(include=['embeddings','documents','metadatas']))

