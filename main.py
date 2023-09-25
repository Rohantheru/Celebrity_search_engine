import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st



os.environ['OPENAI_API_KEY'] = openai_key

st.title('CELEBRITY SEARCH ENGINE')
input_text = st.text_input("Input your text here.")

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))