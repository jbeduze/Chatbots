import streamlit as st

st.header ("simple Echobot")

with st.expander("Descriptions and features"):
  st.write("just a nice set up for chatbots!")

#initiailing chat history
with st.expander("Chatbot", expanded=True):
  if "messages" not in st.session_state:
      st.session_state.message = []
#display chat message from history
  for message in st.session_state.message:
    with st.chat_message(message["role"]):
      st.markdown(messsage["content"])
#react to user input
  if prompt := st.chat_input():
    with st.chat_message("user"):
      st.markdown(prompt)
#user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
  
    response = f"echo: {prompt}"
    with st.chat_message("assistant"):
      st.markdown(response)
  #assistant messsage to chat history  
    st.session_state.message.append({"role": "assistant", "content": response})
