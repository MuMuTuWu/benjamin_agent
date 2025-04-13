import streamlit as st

# 创建两列布局，左列放图片，右列放标题
col1, col2 = st.columns([1, 5])  # 比例为1:5，可以根据需要调整

with col1:
    st.image("assets/artificial-bot-intelligence-svgrepo-com.svg", width=80)
with col2:
    st.title("Introducing Benjamin.AI")

st.markdown("""
Benjamin AI is an intelligent technology company focused on quantitative finance, dedicated to providing advanced financial analysis tools and solutions to investors and institutions. Its core products utilize cutting-edge artificial intelligence technology and data-driven methodologies to cover areas such as portfolio management, risk assessment, trading strategy development, macroeconomic analysis and stock valuation. By integrating real-time and historical data, Benjamin AI is able to provide users with efficient asset allocation optimization, trading strategy backtesting, and market insight services. As a future-oriented financial intelligence platform, Benjamin AI not only helps users improve decision-making efficiency, but also is committed to pushing the frontiers of financial technology.
""")

st.image("assets/1_benjamin_homepage.png")