import streamlit as st

from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.chat_models import ChatOpenAI

from agent import SQL_SYSTEM_PROMPT, StatefulPythonREPL, execute_sql, generate_df_summary

# Initialize models and tools
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
        temperature=0,
        streaming=True  # Enable streaming output
    )
else:
    st.warning("⚠️ Please enter your DeepSeek API key")

###### Create ToolKit ######
# Initialize stateful REPL environment
stateful_repl = StatefulPythonREPL()

# SQL query tool (with automatic saving to REPL environment)
def sql_query_tool(query: str) -> str:
    df = execute_sql(query)
    stateful_repl.globals['current_df'] = df  # Save to REPL environment
    return generate_df_summary(df)

tools = [
    Tool(
        name="sql_query",
        func=sql_query_tool,
        description=(
            "Used to execute SQL queries and get data summaries. Input must be a valid SQL query statement. "
            "After execution, results will be saved to current_df variable for Python code use."
        )
    ),
    Tool(
        name="python_repl",
        description="A Python shell. Only the numpy, pandas, and pypfopt libraries are installed in this Python environment. Use this to execute python code and retain variable states. You can access the current_df variable to process data. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
        func=stateful_repl.run
    )
]

###### Sidebar Layout ######
with st.sidebar:
    st.divider()    
    # Add thought process display control
    st.subheader("Thought Process Display Settings")
    if "expand_new_thoughts" not in st.session_state:
        st.session_state.expand_new_thoughts = True
    if "collapse_completed_thoughts" not in st.session_state:
        st.session_state.collapse_completed_thoughts = False
    
    st.session_state.expand_new_thoughts = st.checkbox(
        "Expand New Thoughts", 
        value=st.session_state.expand_new_thoughts,
        help="When checked, AI's new thought processes will be automatically expanded"
    )
    
    st.session_state.collapse_completed_thoughts = st.checkbox(
        "Collapse Completed Thoughts", 
        value=st.session_state.collapse_completed_thoughts,
        help="When checked, AI's completed thought processes will be automatically collapsed"
    )
    st.divider()
    # Add "New Chat" button to sidebar
    if st.button("🔄 New Chat"):
        st.session_state.messages = [{"role": "assistant", "content": "Hello, I'm your SQL data analysis assistant. How can I help you?"}]
        st.rerun()

###### Main Page Layout ######
st.title("💬 SQL Data Analysis Agent")
st.caption("🚀 A SQL Data Analysis Assistant Powered by DeepSeek-V3-0324")

# Add system prompt editing area
if "custom_system_prompt" not in st.session_state:
    st.session_state.custom_system_prompt = SQL_SYSTEM_PROMPT
with st.expander("System Prompt", expanded=True):
    st.session_state.custom_system_prompt = st.text_area(
        label="Modify the system prompt to change the AI assistant's behavior and response style.",
        value=st.session_state.custom_system_prompt,
        height=170
    )

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello, I'm your SQL data analysis assistant. How can I help you?"}
    ]

###### Create Agent ######
# Initialize memory system
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Create Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=15,
    system_message=st.session_state.custom_system_prompt  # Add custom system prompt
)

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder=""):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").text(prompt)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(
            st.container(),
            max_thought_containers=4,
            expand_new_thoughts=st.session_state.expand_new_thoughts,
            collapse_completed_thoughts=st.session_state.collapse_completed_thoughts
        )
        response = agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
