from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
give me the name, age and city of a fictional person

{format_instructions}
""",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

prompt = template.format()

result = model.invoke(prompt)
#print(result.content)
parsed_result = parser.parse(result.content)
print(parsed_result)