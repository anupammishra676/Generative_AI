from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Select. . .", "Attention is all you need",  "BERT: Pre-training of deep bidirectional transformers", "GPT- 3: Language models are Few-Shot learners", "Diffusion Model beat GANs on Image synthesis"])

style_input = st.selectbox(" Select Explanation style", ["Beginner-Friendly", "Techical", "Code-Oriented","Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')

if st.button('Summarize'):
    #Chaining of mutiple inputs
    chain = template | model
    result = chain.invoke(
        {
        'paper_input' : paper_input,
        'style_input' : style_input,
        'length_input': length_input
        }
    )
    st.write(result.content)



