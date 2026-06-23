
from langchain_google_genai import ChatGoogleGenerativeAI
from getpass import getpass
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Ensure GOOGLE_API_KEY is available as an environment variable
# You might need to set it in a .env file or Streamlit secrets if not already configured
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv('GOOGLE_API_KEY'))

st.header('Research Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = PromptTemplate.from_template(
    "Summarize the research paper '{paper_input}' in a '{style_input}' style and '{length_input}' length. Make sure the explanation is comprehensive."
)



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)