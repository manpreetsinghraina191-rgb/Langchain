from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel



from langchain_community.document_loaders import TextLoader

loader = TextLoader("cricket.txt",encoding="utf-8")

documents = loader.load()

prompt=PromptTemplate(
    template="Summarize the following text: {poem}",
    input_variables=["poem"]
)
model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY")
)
parser=StrOutputParser()
chain=prompt|model|parser
result=chain.invoke({"poem":documents[0].page_content})
print(result)