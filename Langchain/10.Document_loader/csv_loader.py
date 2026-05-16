from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Langchain\\testDirectory\data.csv')

data = loader.load()

print(data[0])