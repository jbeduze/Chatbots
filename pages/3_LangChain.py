import utils
import streamlit as st
from streamlit_chat import message

from langchain.chains import ConversationChain
from langchain.llms import OpenAI


st.title('Welcome to the Langchain Chatbot')
with st.expander("Description and Features"):
  st.write("RAG, or Retrieval-Augmented Generation- within the context of a language model chatbot, refers to a technique that enhances the chatbot's ability to generate responses by integrating a retrieval component with a generative model. This approach allows the chatbot to pull in relevant information or context from a large database or set of documents in real-time, and then use this information to inform the generation of its responses. The retrieval component helps the chatbot to provide more accurate, informative, and contextually relevant answers by leveraging external knowledge sources, thereby improving the overall quality and utility of its interactions.")
with st.expander("Langchain Chatbot", expanded=True):
  class Basic:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"
    
    def setup_chain(self):
        llm = OpenAI(model_name=self.openai_model, temperature=0, streaming=True)
        chain = ConversationChain(llm=llm, verbose=True)
        return chain
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = Basic()
    obj.main()
