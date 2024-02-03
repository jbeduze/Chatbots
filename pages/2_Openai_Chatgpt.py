import streamlit as st
import time
import openai

st.header('OpenAI Chatbots')
with st.expander("Decsription and features"):
  st.write("""Openai's chagpt software read by python in a streamlit UI.
  
  2 different examples are below. The main difference is where the directions for the chatbot originate.
  
  1st- from within the python code
  
  2nd- from within the OpenAI asssitant creator""")
with st.expander("Assistant created within Streamlit"):
  st.write('Chatgpt Clone')
  OPEN_API_KEY = st.secrets["OPENAI_API_KEY"]

  if "openai_model" not in session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
  #initialize chat history
  if "messages" not in sessions_state:
    st.session_state.messages= []

"---"
    
with st.expander("Assistant created within OpenAI and called to Streamlit"):
  st.write('chat')
  assistant_id = "asst_D1wKhK6VfhH6Cp67HpDaEtaT"
  client = openai

  if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
  if "thread_id" not in st.session_state:
    st.session_state.thread_id = None
  
  openai.api_key= st.streamlit.secrets.toml["openai.api_key"]
  
  if st.button("Start Chat"):
    st.session_state.start_chat= True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread_id
    
  if st.button("Exit Chat"):
    st.session_state.messages = [] #clear the chat history
    st.session_state.start_chat = False #reset the chat state
    st.session_state.thread_id = None
