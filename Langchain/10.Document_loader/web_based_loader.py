from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template= 'Answer the the followin question \n {question} from the following \n {text}',
    input_variables=['question','text']
)

url = 'https://docs.langchain.com/oss/python/langchain/overview'

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'question':'What is langchain','text':docs[0].page_content})

print(result)
