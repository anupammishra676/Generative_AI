from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-5.4-nano", temperature= 1.5) #temperature is used to get the answer creativity

result = model.invoke("why cricket is so famous in india")
#print(result) #prints all the details for payload

print(result.content)