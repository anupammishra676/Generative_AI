from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('Who is vaibhav sooryavanshi')

print(results)

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)

print(search_tool.args_schema.model_json_schema())