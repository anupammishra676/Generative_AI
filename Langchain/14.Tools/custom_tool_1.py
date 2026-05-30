# Using @tool method
from langchain_core.tools import tool

#Three important steps to create a tool
#1. Create a function
#2. Add type hints
#3. Add type decorator

@tool
def multiply(a : int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a" : 3, "b" : 5})

print(result)