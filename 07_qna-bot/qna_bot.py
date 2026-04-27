from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

st.title("🤖 AskBuddy – AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Google Gemini!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask anything?")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    
    res = llm.invoke(query)
    st.session_state.messages.append({"role": "assistant", "content": res.content})
    with st.chat_message("assistant"):
        st.markdown(res.content)