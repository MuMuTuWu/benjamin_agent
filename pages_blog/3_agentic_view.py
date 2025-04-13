import time
import streamlit as st
from pages_blog.agent_demo_response import BENJAMIN_AI_CAPABILITY, BENJAMIN_AI_TOOLS

st.title("📐 An Agentic View of Benjamin.AI")
st.subheader("📖 Dissect the capabilities of Benjamin.AI")
st.chat_message("user").write("""What can you do for me?""")
if st.button(label="Send", key="button1"):
    chat_container = st.chat_message("assistant") # 创建一个空的聊天消息容器
    message_placeholder = chat_container.empty() # 创建一个空的占位符用于流式显示文本
    # 模拟流式输出
    displayed_message = ""
    for chunk in BENJAMIN_AI_CAPABILITY.split(" "):
        displayed_message += chunk + " "
        message_placeholder.markdown(displayed_message)
        time.sleep(0.015) # 添加短暂延迟以模拟流式效果
st.divider()

st.subheader("⚒️ Tools of Benjamin.AI")
st.chat_message("user").write("""summarize your tool/function in a markdown table with tool/function description, and parameters""")
if st.button(label="Send", key="button2"):
    chat_container2 = st.chat_message("assistant") # 创建一个空的聊天消息容器
    message_placeholder2 = chat_container2.empty() # 创建一个空的占位符用于流式显示文本
    # 模拟流式输出
    displayed_message2 = ""
    for chunk in BENJAMIN_AI_TOOLS.split(" "):
        displayed_message2 += chunk + " "
        message_placeholder2.markdown(displayed_message2)
        time.sleep(0.015) # 添加短暂延迟以模拟流式效果
st.divider()

st.subheader("🏗️ Benjamin.AI Agent Workflow")
st.image("assets/Agent Flow Chart.png", use_container_width=True)