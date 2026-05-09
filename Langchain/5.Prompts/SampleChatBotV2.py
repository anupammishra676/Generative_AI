from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

# Now the problem is - when we have longer chat history it will be difficult to understand which message is sent by whom. it means either by user or AI. To overcome this issue please refer - SampleChatBotV3.py