from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review in a list"]
    summary : Annotated[str, "A brief summary of review"]
    sentiment : Annotated [Literal["Pos", "Neg", "Ntl"], "Generate sentiment which is either positive, negative or neutral"] # Can pass own keywords as well
    pros: Annotated[Optional[list[str]],"Write down all the pros inside a list"]  # Might be optional - import from typing
    cons: Annotated[Optional[list[str]],"Write down all the pros inside a list"]

strucutred_output = model.with_structured_output(Review)

result = strucutred_output.invoke("""
The Good (Pros):
Honestly, the battery life is a beast. I’m a heavy user—lots of streaming and social media—and I’m consistently ending the day with 30% left. It’s such a relief not to hunt for a charger by 6:00 PM. The camera quality is also stunning; the "Night Mode" actually makes low-light photos look crisp instead of a grainy mess. I took some shots at a concert last weekend, and my friends were genuinely jealous of the clarity. Also, the UI is super smooth; I haven't noticed a single lag spike even when I have twenty apps open at once.

The Bad (Cons):
However, it’s not all perfect. The in-display fingerprint sensor is incredibly frustrating. It fails about 30% of the time, especially if my hands are slightly dry, which feels like a major step backward for a "flagship" phone. Another thing—the phone gets uncomfortably hot during fast charging. It’s reached a point where I’m worried about the long-term health of the hardware. Lastly, why did they remove the headphone jack? I know it’s the trend, but the included dongle feels cheap and I’ve already misplaced it once.

Final Thoughts:
I’m a bit torn. When it works, it’s easily the best phone I’ve owned. The screen is gorgeous and the speed is top-tier. But the biometrics bug me every single day, and the heating issues make me nervous. If you can live with the finicky sensor, it’s a great buy, but for $1,000, I expected these basic things to be flawless. It’s a solid 8/10, but that 20% of "annoyance" definitely keeps it from being perfect.
"""
                                  )

print(result)
print(result['summary']) 
print(result['sentiment'])