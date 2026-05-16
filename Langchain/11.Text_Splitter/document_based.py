from langchain_text_splitters import RecursiveCharacterTextSplitter, Language


text = """
class Dog:
    # Class attribute (shared by all instances)
    species = "Canine"

    # The __init__ method (constructor) initializes new objects
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

# Create an object (instance) of the class
my_dog = Dog("Buddy", 3)

# Access attributes and call methods
print(my_dog.name)    # Output: Buddy
print(my_dog.bark())  # Output: Buddy says Woof!
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks[1])