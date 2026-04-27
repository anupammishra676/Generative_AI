from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic()

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short quetion answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge and provide notes and quiz into a single document \n notes -> {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | model1 | parser,
        'quiz' : prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model1 |parser

chain = parallel_chain | merge_chain

text = """
XGBoost (eXtreme Gradient Boosting) is an open-source, high-performance machine learning library that implements optimized gradient-boosted decision trees for regression and classification. It is designed for speed, scalability, and high accuracy, often used in Kaggle competitions and industry for structured data by building trees sequentially to correct previous errors
"""
result = chain.invoke({'text':'text'})

print(result)