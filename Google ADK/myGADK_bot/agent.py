from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

root_agent = Agent(
    #model='gemini-3.5-flash', #use LLM from google family like gemini-3.5-flash, gemini-4, etc
    model=LiteLlm(model="openai/gpt-4o"), #to use other LLMs apart from google family like openai/claude
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=1024
    )
)
