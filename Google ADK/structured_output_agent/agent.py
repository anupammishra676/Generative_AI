from typing import Literal
from pydantic import BaseModel, Field
from google.adk import Agent

# Define the output schema for the agent. It will handle the nullable fields and the list of courses the student is interested in.
class Enquiry(BaseModel):
    name: str | None = Field(default=None, description="Student's full name, properly capitalized")
    email: str | None = Field(default=None, description="Email address exactly as written")
    interested_in: list[Literal["GenAI", "Data Science", "MLOps", "Deep Learning", "Other"]] = Field(
        description="CampusX courses the student is interested in"
    )
    budget_inr: int | None = Field(default=None, ge=0, le=500000,
        description="Total budget in rupees as a plain number. Convert '15k' to 15000")

root_agent = Agent(
    name="enquiry_agent",
    model="gemini-3.5-flash",
    description="Extracts student enquiry details from a message.",
    instruction="Read the student's message and extract their details. "
                "If something is not mentioned, leave it empty. Never guess.",
    output_schema=Enquiry, # define the output schema for the agent
    output_key='enquiry' # Use to save the output in a dictionary with the key 'enquiry' which acts as state for the agent
)