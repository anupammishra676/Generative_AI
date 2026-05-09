from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI() #Load default model or you can mention it 

while True:
    user_input = input('You : ')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("AI: ",result.content)


# Now the problem is - it is not storing the context or previous messages. To ovecome this issue we need to maintain chat hisotry - Refer SampleChatBotV2.py