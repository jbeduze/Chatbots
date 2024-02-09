import openai
import streamlit as st

st.title("ChatGPT-like clone")

# Assuming you've set the API key in your Streamlit secrets correctly
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversations
for message in st.session_state.messages:
    with st.container():
        st.write(f"{message['role']}: {message['content']}")

# Input from the user
prompt = st.text_input("What is up?")
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        # Append the AI's response to the conversation history
        st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message['content']})
    except Exception as e:
        st.error(f"Error calling OpenAI: {str(e)}")

# Optionally, display the conversation after adding the new messages
for message in st.session_state.messages:
    with st.container():
        st.write(f"{message['role']}: {message['content']}")



# import openai
# from openai import OpenAI
# import streamlit as st

# st.title("ChatGPT-like clone")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-4"
    
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         stream = client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )
#         response = st.write_stream(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response})


# import streamlit as st
# import openai
# from openai import OpenAI
# import time

# st.header('OpenAI Simple Chatbots')
               
# with st.expander("Description and Features"):
#   st.write("""Openai's chagpt software read by python in a streamlit UI.
#     2 different examples are below. The main difference is where the directions for the chatbot originate.
#     1st- from within the python code- Streamlit provides code for the build out of this app: https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps as well as the youtube video: https://www.youtube.com/watch?v=sBhK-2K9bUc&t=303s 
#     2nd- from within the OpenAI asssitant creator"""
#   )

# with st.expander("Assistant created within Streamlit"):
#     openai.api_key= st.secrets["OPENAI_API_KEY"]
#       # Initialize session state for openai_model
#     if "openai_model" not in st.session_state:
#       st.session_state["openai_model"] = "gpt-3.5-turbo"
  
#   # Initialize session state for messages
#     if "messages" not in st.session_state:
#       st.session_state.messages = []
#   # Display existing messages
#     for message in st.session_state.messages:
#       with st.chat_message(message["role"]):
#           st.markdown(message["content"])

#     if prompt:= st.chat_input("How's it hanging?"):
#       with st.chat_message("user"):
#           st.markdown(prompt)
#       st.session_state.messages.append({"role": "user", "content": prompt})
      
#       with st.chat_message("assistant"):
#           message_placeholder = st.empty()
#           full_response = ""
#           for response in openai.ChatCompletion.create(
#               model=st.session_state["openai_model"],
#               messages=[
#                   {"role": m["role"], "content": m["content"]}
#                   for m in st.session_state.messages
#               ],
#               stream=True)
#           response = st.write_stream(stream)
#       st.session_state.messages.append({"role": "assistant", "content": response})
#_____________________________________________________________________________________________
# Correct the API Key access
#openai.api_key = st.secrets["OPENAI_API_KEY"]

# Example correction for thread creation and message handling in OpenAI Assistant
# This is more of a placeholder as the actual implementation would depend on OpenAI's API


# import streamlit as st
# import time
# import openai

# if "openai_model" not in session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# st.header('OpenAI Chatbots')
# with st.expander("Decsription and features"):
#   st.write("""Openai's chagpt software read by python in a streamlit UI.
  
#   2 different examples are below. The main difference is where the directions for the chatbot originate.
  
#   1st- from within the python code- Streamlit provides code for the build out of this app: https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps as well as the youtube video: https://www.youtube.com/watch?v=sBhK-2K9bUc&t=303s 
  
#   2nd- from within the OpenAI asssitant creator""")
  
# with st.expander("Assistant created within Streamlit"):
#   st.write('Chatgpt Clone')
#   openai.api_key = st.secrets["OPENAI_API_KEY"]

#   if "openai_model" not in session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"
#   #initialize chat history
#   if "messages" not in sessions_state:
#     st.session_state.messages= []

#   for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#       st.markdown(message["content"])

#   prompt = st.chat_input("what's up")
#   if prompt:
#     with st.chat_message("user"):
#       st.markdown(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})

#   #response
#     with st.chat_message("asssistant"):
#       message_placeholder = st.empty()
#       full_response = ""
#       for response in openai.chatcompletion.create(
#         model=st.session_state["openai_model"],
#         messages=[
#           {"role": m["role"], "content": m["content"]}
#           for m in st.session_state.messages
#         ],
#         stream=True,
#       ):
#         full_response += response.choices[0].delta.get("content", "")
#   st.session_state.messages.append({"role": "assistant", "content": full_response})   

# "---"
    
# with st.expander("Assistant created within OpenAI and called to Streamlit"):
#   st.write('chat')
#   assistant_id = "asst_D1wKhK6VfhH6Cp67HpDaEtaT"
#   client = openai

#   if "start_chat" not in st.session_state:
#     st.session_state.start_chat = False
#   if "thread_id" not in st.session_state:
#     st.session_state.thread_id = None
  
#   openai.api_key= st.streamlit.secrets.OPENAI_API_KEY
  
#   if st.button("Start Chat"):
#     st.session_state.start_chat= True
#     thread = client.beta.threads.create()
#     st.session_state.thread_id = thread_id
    
#   if st.button("Exit Chat"):
#     st.session_state.messages = [] #clear the chat history
#     st.session_state.start_chat = False #reset the chat state
#     st.session_state.thread_id = None
