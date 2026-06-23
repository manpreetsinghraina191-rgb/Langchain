from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
class Person(BaseModel):
    name: str = Field(description="the name of the person")
    age: int = Field(description="the age of the person")
    city: str = Field(description="the city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template="give me the name, age and city of a fictional person\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)
prompt=template.format()
result=model.invoke(prompt)
parsed_result=parser.parse(result.content)
print(parsed_result)

