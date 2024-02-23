import openai
import streamlit as st

st.title("ChatGPT-like clone")

# Assuming you've set the API key in your Streamlit secrets correctly
openai.api_key = st.secrets["API_KEY"]

#
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"
#initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversations
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from the user
prompt = st.text_input("What is up?")
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": prompt})

if prompt := st.chat_input("Write a question and hit the submit button!"):
    
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

