from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY"))
prompt=PromptTemplate(
    template="write 5 intresting facts about {topic}",
    input_variables=["topic"]
)
parser=StrOutputParser()
chain=prompt | model | parser
result=chain.invoke({"topic": "black holes"})
print(result)
chain.get_graph().print_ascii()