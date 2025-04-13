import streamlit as st

st.title("🔍 Capabilities Validation")

st.header("📖 Capabilities Summary")

st.markdown("""**Core Competencies**

- Investment analysis, portfolio management, trading strategies, and economic research.

**Comprehensive Asset Coverage**

- Analyzes equities, cryptocurrencies, forex, and commodities.
- Synthesizes real-time data with historical metrics to generate actionable insights.

**Portfolio Management Features**

- Uses advanced algorithms for asset allocation and risk management.
- Focus on backtesting and performance benchmarking and risk-return optimization.

**Economic Contextualization**

- Integrates macroeconomic analysis of indicators, interest rates, and global economic trends.

**Integrated Financial Solution**

- Combines computational analysis with market intelligence for data-driven investment insights.

- Serves as an educational resource for investment methodologies and market mechanics.""")

st.divider()

st.header("🔍 Accuracy Test")
st.subheader("Result comparison (TSLA Market Beta)")

st.markdown("""
- Testing Objective
- Method Overview
- Results
- Conclusion and Limitations""")

st.markdown("**Our team Code-Based Approach**")
# st.image("assets/validation 1.png")
st.image("assets/validation 2.png")

st.markdown("**Benjamin.AI result**")
st.image("assets/validation 3.png")
st.divider()

st.subheader("Result comparison (TSLA Rolling beta)")
st.markdown("""- Long-term Beta Analysis
- Beta Calculations with Rolling Window Approach
- Short-term (22-day) vs. Long-term (252-day) Volatility""")
st.markdown("""
|  | Code | Benjamin.AI |
|------------|------|------------|
| Long Term Rolling Beta | 1.51 | 1.85 |
| Short Term Rolling Beta | 1.58 | Not Avaliable |""")
# st.markdown("**Our team Code-Based Approach**")
# col1, col2 = st.columns([0.5, 0.5], gap="large")
# with col1:
#     st.image("assets/validation 5.png")
# with col2:
#     st.image("assets/validation 6.png")
# st.markdown("**Benjamin.AI result**")
# st.image("assets/validation 4.png")

st.divider()

st.subheader("Result comparison (OPTIMAL PORTFOLIO)")
st.markdown("""- Test Objective
- Data and Methodology
- Python Results
- Benjamin AI Results
- Validation Conclusion""")
st.markdown("""
| Performance | Code | Benjamin.AI |
|------------|------|------------|
| Annual Return | 9.40% | 3.23% |
| Annual Volatility | 11.50% | 11.54% |
| Sharpe Ratio | 0.68 | 0.28 |""")
st.markdown("**Our team Code-Based Approach**")
st.image("assets/validation 7.png")
st.markdown("**Benjamin.AI result**")
st.image("assets/validation 8.png")