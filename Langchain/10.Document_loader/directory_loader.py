from langchain_community.document_loaders import DirectoryLoader,TextLoader

loader = DirectoryLoader(
    path = 'Langchain\\testDirectory',
    glob = '*.txt',
    loader_cls = TextLoader
)

# docs = loader.load()

docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)