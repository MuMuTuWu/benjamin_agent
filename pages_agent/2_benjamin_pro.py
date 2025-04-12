import streamlit as st

from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.chat_models import ChatOpenAI

from agent import SQL_SYSTEM_PROMPT, StatefulPythonREPL, execute_sql, generate_df_summary

# 初始化模型和工具
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

if not st.session_state.clickhouse_password or st.session_state.clickhouse_password.strip() == "":
    st.warning("⚠️ Please enter your ClickHouse password")

# Create DeepSeek LLM
if st.session_state.openai_api_key and st.session_state.openai_api_key.strip() != "":
    llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=st.session_state.openai_api_key,
        base_url="https://api.deepseek.com/v1",
        temperature=0.3,
        streaming=True  # Enable streaming output
    )
else:
    st.warning("⚠️ Please enter your DeepSeek API key")

###### Create ToolKit ######
# 初始化带状态的REPL环境
stateful_repl = StatefulPythonREPL()

# SQL查询工具（带自动保存到REPL环境）
def sql_query_tool(query: str) -> str:
    df = execute_sql(query)
    stateful_repl.globals['current_df'] = df  # 保存到REPL环境
    return generate_df_summary(df)

tools = [
    Tool(
        name="sql_query",
        func=sql_query_tool,
        description=(
            "用于执行SQL查询并获取数据摘要。输入必须是有效的SQL查询语句。"
            "执行后会保存结果到current_df变量供Python代码使用。"
        )
    ),
    Tool(
        name="python_repl",
        description="执行Python代码并保留变量状态。可以访问current_df变量处理数据。",
        func=stateful_repl.run
    )
]

###### Sidebar Layout ######
with st.sidebar:
    st.divider()
    # Add "New Chat" button to sidebar
    if st.button("🔄 New Chat"):
        st.session_state.messages = [{"role": "assistant", "content": "Hello, I'm your SQL assistant. How can I help you?"}]
        st.rerun()

###### Main Page Layout ######
st.title("💬 SQL Agent")
st.caption("🚀 A SQL Query Assistant Powered by DeepSeek-V3-0324")

# Add system prompt editing area
if "custom_system_prompt" not in st.session_state:
    st.session_state.custom_system_prompt = SQL_SYSTEM_PROMPT
with st.expander("System Prompt", expanded=True):
    st.session_state.custom_system_prompt = st.text_area(
        label="Modify the system prompt to change the AI assistant's behavior and response style.",
        value=st.session_state.custom_system_prompt,
        height=150
    )

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

###### Create Agent ######
# 初始化记忆系统
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 创建Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=15,
    system_message=st.session_state.custom_system_prompt  # 添加自定义系统提示
)

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").text(prompt)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(
            st.container(),
            max_thought_containers=4,
            expand_new_thoughts=True,
            collapse_completed_thoughts=False
        )
        response = agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
