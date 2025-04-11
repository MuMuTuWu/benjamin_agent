import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.base import BaseCallbackHandler

import time
import simplejson as json

if not st.session_state.clickhouse_password:
    st.warning("Please enter your ClickHouse password")

# Define system prompt
system_prompt = """You are a professional SQL query assistant, specialized in helping users write and optimize ClickHouse database queries.
Please follow these rules:
1. When users request SQL queries, provide clear and efficient ClickHouse SQL code
2. Explain key parts of the query and optimization logic
3. If user requests are unclear, ask questions to get more information
4. For complex queries, provide optimization suggestions considering ClickHouse performance characteristics
5. Answer user questions in English
"""

# Create DeepSeek LLM
if st.session_state.openai_api_key:
    llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=st.session_state.openai_api_key,
        base_url="https://api.deepseek.com/v1",
        temperature=0.3,
        streaming=True  # Enable streaming output
    )
else:
    st.warning("Please enter your DeepSeek API Key")

# Create streaming output callback handler
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text
        self.run_id = None
        
    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.container.markdown(self.text)

st.title("💬 SQL Agent")
st.caption("🚀 A SQL Query Assistant Powered by DeepSeek LLM")

# Add system prompt editing area
if "custom_system_prompt" not in st.session_state:
    st.session_state.custom_system_prompt = system_prompt

with st.expander("Custom System Prompt", expanded=True):
    st.session_state.custom_system_prompt = st.text_area(
        "Edit system prompt to customize AI assistant behavior",
        value=st.session_state.custom_system_prompt,
        height=200
    )
    st.caption("Tip: Modify the system prompt to change the AI assistant's behavior and response style.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I'm your SQL assistant. How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not st.session_state.openai_api_key:
        st.info("Please enter your DeepSeek API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Create an empty message container for streaming output
    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        # Create message list using custom system prompt and user input
        messages = [
            SystemMessage(content=st.session_state.custom_system_prompt),
            HumanMessage(content=prompt)
        ]
        response = llm.generate([messages], callbacks=[stream_handler])
        msg = stream_handler.text
        
    # Add complete response to chat history
    st.session_state.messages.append({"role": "assistant", "content": msg})