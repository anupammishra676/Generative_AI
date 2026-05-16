from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),breakpoint_threshold_type="standard_deviation",breakpoint_threshold_amount=0.5
)

sample = """
Farmers are the backbone of india. India loves cricket and IPL is one of the most loving tournament

Indian politics are revolve around BJP. Narendra modi is the leader of BJP.
"""

docs = text_splitter.create_documents([sample])

print(docs)