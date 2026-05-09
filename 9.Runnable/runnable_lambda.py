# Apply custom python functions and convert into runnable



#                        |----- Passthrough --------- Joke
# prompt - LLM - parser -                               | ------ Output
#                        |----- Runnable Lambda ----- Words

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template = 'Generate a joke about the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate the explanation of {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser),
    'word_count' : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic' : 'MMA'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)