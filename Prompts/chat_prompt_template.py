from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
template = ChatPromptTemplate([
    ('system', "You are a helpful assistant that provides information about {domain}."),
    ('human', "What can you tell me about {topic}?")
    
])
prompt=template.invoke({
    'domain': 'cricket',
    'topic': 'LBW'
 })
print(prompt)