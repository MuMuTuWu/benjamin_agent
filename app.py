import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="Benjamin.AI",
    page_icon="assets/artificial-bot-intelligence-svgrepo-com.svg",
    layout="centered",
    initial_sidebar_state="expanded",
)

pages = {
    "Blogs": [
        st.Page("blogs/1_introduction.py", title="Introducing Benjamin.AI", icon="👋"),
        st.Page("blogs/2_capability_validation.py", title="Capability Validation", icon="🔍"),
        st.Page("blogs/3_agentic_view.py", title="An Agentic View of Benjamin.AI", icon="📐"),
    ],
    "Agents": [
        st.Page("agents/sql_agent.py", title="SQL Agent", icon="🤖"),
        st.Page("agents/benjamin_pro.py", title="Benjamin.AI Pro", icon="🤖"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()