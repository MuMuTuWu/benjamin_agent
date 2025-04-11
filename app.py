import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="Benjamin.AI",
    page_icon="assets/artificial-bot-intelligence-svgrepo-com.svg",
    layout="centered",
    initial_sidebar_state="expanded",
)


# TODO: 记得删除 keys
# 初始化session_state中的clickhouse_password（如果不存在）
if "clickhouse_password" not in st.session_state:
    st.session_state.clickhouse_password = ""

# 初始化session_state中的openai_api_key（如果不存在）
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""


with st.sidebar:
    clickhouse_password = st.text_input(
        "Clickhouse Password",
        value=st.session_state.clickhouse_password,
        type="password",
        key="clickhouse_password_input"
    )
    if clickhouse_password:
        st.session_state.clickhouse_password = clickhouse_password

    # 使用session中已有的值作为默认值，并在用户输入后更新session
    openai_api_key = st.text_input(
        "DeepSeek API Key", 
        value=st.session_state.openai_api_key,
        type="password",
        key="api_key_input"
    )
    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key

    "[Get an DeepSeek API key](https://platform.deepseek.com/api_keys)"


pages = {
    "Blogs": [
        st.Page("blogs/1_introduction.py", title="Introducing Benjamin.AI", icon="👋"),
        st.Page("blogs/2_capability_validation.py", title="Capability Validation", icon="🔍"),
        st.Page("blogs/3_agentic_view.py", title="An Agentic View of Benjamin.AI", icon="📐"),
    ],
    "Agents": [
        st.Page("agents/1_sql_agent.py", title="SQL Agent", icon="🤖"),
        st.Page("agents/2_benjamin_pro.py", title="Benjamin.AI Pro", icon="🤖"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()