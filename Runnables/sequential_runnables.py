from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os
load_dotenv()
prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)
model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY")
)
print(os.getenv("GOOGLE_API_KEY"))
parser=StrOutputParser()
chain=RunnableSequence(prompt,model,parser)
result=chain.invoke({"topic":"AI"})
print(result)
