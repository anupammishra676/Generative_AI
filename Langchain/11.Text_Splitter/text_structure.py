from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap= 0
)

loader = TextLoader('politics.txt', encoding = 'utf-8')

docs = loader.load()

chunks = splitter.split_documents(docs)

print(chunks)