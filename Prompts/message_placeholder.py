from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
chat_template=ChatPromptTemplate([
    ('system',"you are a helpful customer support assistant for a software company that provides technical assistance to users."),
    MessagesPlaceholder(variable_name='chat_history' ),
    ('human','{query}')
])
chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)
prompt=chat_template.invoke({
    'chat_history': chat_history,
    'query': "what about my refund?"
})
print(prompt)
