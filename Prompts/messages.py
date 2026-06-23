from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv('GOOGLE_API_KEY'))
messages =[
    SystemMessage(content="You are a helpful assistant that provides information about the latest advancements in AI research."),
    HumanMessage(content="What are the latest advancements in AI research?"),
]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)

