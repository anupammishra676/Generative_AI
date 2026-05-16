from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI()

parser = StrOutputParser()

loader = TextLoader('politics.txt', encoding = 'utf-8')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10,  #Use establish to Co-relation between two chunks. it will help to retain context
    separator=''
)

result = splitter.split_documents(docs) #Pass entire document
#result = splitter.split_text(docs[0].page_content)  --> Specific to any doc

print(result[0].page_content)

 