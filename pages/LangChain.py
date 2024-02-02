import streamlit as st
from streamlit_chat import message

from langchain.chains import ConversationChain
from langchain.llms import OpenAI


st.title('Welcome to the Langchain Chatbot')
with st.expander("Description and Features"):
  st.write("RAG, or Retrieval-Augmented Generation- within the context of a language model chatbot, refers to a technique that enhances the chatbot's ability to generate responses by integrating a retrieval component with a generative model. This approach allows the chatbot to pull in relevant information or context from a large database or set of documents in real-time, and then use this information to inform the generation of its responses. The retrieval component helps the chatbot to provide more accurate, informative, and contextually relevant answers by leveraging external knowledge sources, thereby improving the overall quality and utility of its interactions.")
with st.expander("Langchain Chatbot", expanded=True):
  def load_chain():
    llm = OpenAI(temperature=5)

  message("Hello, how are you")
