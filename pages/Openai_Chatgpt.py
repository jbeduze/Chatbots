import streamlit as st

st.header('OpenAI Chatbots')
with st.expander("Decsription and features"):
  st.write("""Openai's chagpt software read by python in a streamlit UI.
  
  2 different examples are below. The main difference is where the directions for the chatbot originate.
  
  1st- from within the python code
  
  2nd- from within the OpenAI asssitant creator""")
with st.expander("Assistant created within Streamlit"):
  st.write('chat')
  assistant = client.beeta.assistant.create(
    name="
with st.expander("Assistant created within OpenAI and called to Streamlit"):
  st.write('chat')

