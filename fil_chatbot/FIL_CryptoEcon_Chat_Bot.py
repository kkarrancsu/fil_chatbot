import streamlit as st

from kb import KBManager
from chatbot import ChatBot
from langchain import hub
import asyncio
from typing import Any, AsyncIterator, Dict, List, Literal, Union, cast
from langchain_core.outputs import LLMResult
from langchain.callbacks.base import AsyncCallbackHandler
from langchain.callbacks.streaming_aiter import AsyncIteratorCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import glob

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "fil_chatbot"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__df28b9de08c04342ad24c0d5423e8030"

def clear_history():
    st.session_state.pop("messages", None)
    st.session_state.ce_chatbot.clear_history()

with st.spinner('Loading Knowledgebase...'):
    if 'kb' in st.session_state:
        kb = st.session_state.kb
    else:
        kb = KBManager(persist_directory="fil_chatbot/filecoin_kb")
        st.session_state.kb = kb
with st.spinner('Loading Chatbot...'):
    if 'llm' in st.session_state:
        llm = st.session_state.llm
    else:
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0,
            convert_system_message_to_human=True,
            max_tokens=16384,
        )
        st.session_state.llm = llm
if 'ce_chatbot' in st.session_state:
    ce_chatbot = st.session_state.ce_chatbot
else:
    ce_chatbot = ChatBot(llm=llm, kb=kb)
    st.session_state.ce_chatbot = ce_chatbot

# st.title("🚀 A CE Chatbot")
st.markdown("[![CryptoEconLab](./app/static/cover.png)](https://cryptoeconlab.io)")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ce_chatbot(prompt)
            # answer = response["answer"]
            answer = response
            st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

with st.sidebar:
    st.button("New Session", on_click=clear_history)