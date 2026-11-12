from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instructioninstruction=(
        "Answer user questions accurately. "
        "Use Google Search when you need current information "
        "or need to verify facts."
    ),
    tools=[google_search],
)
