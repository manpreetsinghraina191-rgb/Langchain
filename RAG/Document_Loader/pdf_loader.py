from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("dl-curriculum.pdf")
docsuments = loader.load()
print(docsuments[0].page_content)
