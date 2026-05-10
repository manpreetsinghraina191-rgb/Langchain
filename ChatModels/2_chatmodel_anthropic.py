from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
llm=ChatAnthropic(model="claude-2")

result=llm.invoke("What is the capital of India?")
print(result.content)
