import streamlit as st

# 创建两列布局，左列放图片，右列放标题
col1, col2 = st.columns([1, 5])  # 比例为1:5，可以根据需要调整

with col1:
    st.image("assets/artificial-bot-intelligence-svgrepo-com.svg", width=80)
with col2:
    st.title("Introducing Benjamin.AI")

st.markdown("""**Company Focus**

- An intelligent technology company focused on quantitative finance for investors and institutions.

**Core products and technologies**

- Utilizes cutting-edge artificial intelligence technology and data-driven methodologies.
- Covering areas such as portfolio management, risk assessment, trading strategy development, macroeconomic analysis and stock valuation.

**Functions and Services**

- Provide asset allocation optimization by integrating real-time and historical data.
- Supports trading strategy backtesting and market insight services.

**Future Vision**

- Improve the efficiency of users' decision-making.
- Dedicated to advancing the development of financial technology.""")

st.image("assets/1_benjamin_homepage.png")