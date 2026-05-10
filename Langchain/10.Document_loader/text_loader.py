from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template= 'Summarize the report - \n {report}',
    input_variables=['report']
)

loader = TextLoader('politics.txt', encoding = 'utf-8')

docs = loader.load()

print(docs)

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'report' : docs[0].page_content}))