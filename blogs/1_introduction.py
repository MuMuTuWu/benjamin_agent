import streamlit as st

# 创建两列布局，左列放图片，右列放标题
col1, col2 = st.columns([1, 5])  # 比例为1:5，可以根据需要调整

with col1:
    st.image("assets/artificial-bot-intelligence-svgrepo-com.svg", width=80)
with col2:
    st.title("Introducing Benjamin.AI")

st.markdown("""
    Benjamin.AI is an AI assistant that can help you with a wide range of tasks, from answering questions to generating text.
    It is powered by the latest AI technology and is constantly improving.
    You can try it out by clicking the button below.
""")

st.image("assets/1_benjamin_homepage.png")