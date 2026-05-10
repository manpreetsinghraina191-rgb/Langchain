from lanchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=["delhi is the capital of india","mumbai is the financial capital of india"]
result=embedding.embed_documents(documents)
print(str(result))