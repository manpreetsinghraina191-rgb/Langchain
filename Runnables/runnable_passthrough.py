from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough
import os
load_dotenv()
prompt1=PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Generate a LinkedIn post about {topic}",

    input_variables=["topic"]

)
model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY")
)
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chaim=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2,model,parser)
})
final_chain=RunnableSequence(joke_gen_chain,parallel_chaim)
result=final_chain.invoke({"topic":"cricket"})
print(result)