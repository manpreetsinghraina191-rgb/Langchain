from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
schema=[
    ResponseSchema(name="fact1",description="the first fact about the topic"),
    ResponseSchema(name="fact2",description="the second fact about the topic"),
    ResponseSchema(name="fact3",description="the third fact about the topic")
]
parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template="give me 3 facts about {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)
prompt=template.invoke({"topic": "black holes"})
result=model.invoke(prompt)
parsed_result=parser.parse(result.content)
print(parsed_result)