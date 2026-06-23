from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv('GOOGLE_API_KEY'))
Chathistory = []
while(True):
    user_input=input("You: ")
    Chathistory.append({"role": "user", "content": user_input})
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(Chathistory)
    Chathistory.append({"role": "assistant", "content": response.content})
    print("Chatbot:", response.content)

print(Chathistory)