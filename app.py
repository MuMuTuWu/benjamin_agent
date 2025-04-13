import streamlit as st
import os
from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')

# 加载.env文件中的环境变量
load_dotenv()

# 设置页面配置
st.set_page_config(
    page_title="Benjamin.AI",
    page_icon="assets/artificial-bot-intelligence-svgrepo-com.svg",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 初始化session_state中的clickhouse_password（如果不存在）
if "clickhouse_password" not in st.session_state:
    st.session_state.clickhouse_password = os.getenv("CLICKHOUSE_PASSWORD", "")

# 初始化session_state中的openai_api_key（如果不存在）
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = os.getenv("OPENAI_API_KEY", "")


with st.sidebar:
    # 直接使用主要的session_state变量作为key
    st.text_input(
        "Clickhouse Password",
        value=st.session_state.clickhouse_password,
        type="password",
        key="clickhouse_password"  # 直接使用主变量作为key
    )

    st.text_input(
        "DeepSeek API Key",
        value=st.session_state.openai_api_key,
        type="password",
        key="openai_api_key"  # 直接使用主变量作为key
    )

    "[Get an DeepSeek API key](https://platform.deepseek.com/api_keys)"


pages = {
    "Blogs": [
        st.Page("pages_blog/1_introduction.py", title="Introducing Benjamin.AI", icon="👋"),
        st.Page("pages_blog/2_capability_validation.py", title="Capability Validation", icon="🔍"),
        st.Page("pages_blog/3_agentic_view.py", title="An Agentic View of Benjamin.AI", icon="📐"),
        st.Page("pages_blog/4_pricing.py", title="Pricing", icon="💰"),
    ],
    "Agents": [
        st.Page("pages_agent/1_sql_agent.py", title="SQL Data Analysis Agent", icon="💬"),
        st.Page("pages_agent/2_benjamin_pro.py", title="Benjamin.AI Pro", icon="🤖"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()