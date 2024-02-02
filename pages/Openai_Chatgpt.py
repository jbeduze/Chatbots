import streamlit as st
import time
import openai

st.header('OpenAI Chatbots')
with st.expander("Decsription and features"):
  st.write("""Openai's chagpt software read by python in a streamlit UI.
  
  2 different examples are below. The main difference is where the directions for the chatbot originate.
  
  1st- from within the python code
  
  2nd- from within the OpenAI asssitant creator""")
# with st.expander("Assistant created within Streamlit"):
#   st.write('chat')
#   assistant = client.beta.assistant.create(
#     name="Health Guru")
with st.expander("Assistant created within OpenAI and called to Streamlit"):
  st.write('chat')
  assistant_id = "asst_D1wKhK6VfhH6Cp67HpDaEtaT"
  client = openai

  if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
  if "thread_id" not in st.session_state:
    st.session_state.thread_id = None
  
  openai.api_key= st.secrets["openai.api_key"]
  
  if st.button("Start Chat"):
    st.session_state.start_chat= True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread_id
    
  if st.button("Exit Chat"):
    st.session_state.messages = [] #clear the chat history
    st.session_state.start_chat = False #reset the chat state
    st.session_state.thread_id = None
