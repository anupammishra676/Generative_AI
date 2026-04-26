from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):

    #Plain dict - Sometime LLM might confuse to overcome this use Annotated TypedDict(See Below)
    # summary: str
    # sentiment: str

    #Annotated dict - Import annotated from typing 
    summary : Annotated[str, "A brief summay of review"]
    sentiment : Annotated[str, "Return sentiment of the review either positive, negative or neutral"]



structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Phone is smooth and value for money. Look and feel seems quite handy. The sound quality is high, camera could have better. 8GB RAM is okay, however 12 GB is recommended. Overall, a mid variant phone that you can explore.""")

print(result)
print(result['summary'])
print(result['sentiment'])

