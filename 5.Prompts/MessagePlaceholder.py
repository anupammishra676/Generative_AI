from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

chat_template = ChatPromptTemplate(
    [
        ('system', 'you are a helpful customer support agent'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{query}')
    ]
)

chat_history = []

with open('5.Prompts/chat_history.txt') as f:
    for line in f:
        if line.startswith("Human:"):
            chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
        elif line.startswith("AI:"):
            chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'Where is my refund'
})

response = model.invoke(prompt)
print(response.content)