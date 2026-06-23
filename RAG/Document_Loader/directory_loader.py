from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader
loader = DirectoryLoader(
    path="Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()
print(documents[0].page_content)