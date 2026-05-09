# Work as a if else



#                        |----- > 500 words --------- Summarize
# prompt - LLM - parser -                               
#                        |----- else -----             Report

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template = 'Generate a report about the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summaraize the give {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500 , RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic' : 'Russia vs Ukraine'})

print(result)