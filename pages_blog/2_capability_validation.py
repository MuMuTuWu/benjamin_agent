import streamlit as st

st.title("🔍 Capability Validation")

st.markdown("""
Benjamin.AI functions as a sophisticated financial intelligence platform that integrates four core competencies: investment analysis, portfolio management, trading strategies, and economic research. The system conducts comprehensive technical and fundamental analysis across multiple asset classes—equities, cryptocurrencies, forex, and commodities—synthesizing real-time data with historical metrics to generate actionable insights.

In portfolio management, Benjamin implements advanced optimization algorithms for asset allocation and risk management, while its trading functionality offers robust backtesting and performance benchmarking with emphasis on risk-reward optimization. The platform contextualizes investment decisions through macroeconomic analysis of indicators, interest rates, and global economic developments.

Benjamin.AI represents an integrated solution for financial decision-making, combining computational analysis with market intelligence to deliver data-driven investment insights while simultaneously serving as an educational resource on investment methodologies and market mechanics.
""")
st.divider()

st.markdown("### ACCURACY TEST (1): TESLA'S MARKET BETA")

st.markdown("#### Our team Code-Based Approach")
st.image("assets/validation 1.png")
st.image("assets/validation 2.png")

st.markdown("#### Benjamin.AI result")
st.image("assets/validation 3.png")
st.markdown("""Although the methods used were not exactly consistent, the errors were within acceptable limits and they barely passed the test.""")
st.divider()

st.markdown("### ACCURACY TEST (2): Rolling Beta")
st.markdown("#### Benjamin.AI result")
st.image("assets/validation 4.png")
col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    st.image("assets/validation 5.png")
with col2:
    st.image("assets/validation 6.png")
st.markdown("Benjamin AI's analysis provides a long-term Beta curve for Tesla, noting an average Beta of 1.85 for 2010-2024 and emphasizing that its volatility will rise over time, particularly in 2021-2024 when it peaks at 2.5. However, the AI's results are based on a rolling window (likely 252 days) and lack short-term volatility details. In contrast, our analysis calculates rolling 22-day and 252-day betas, which provide a comprehensive picture of both the short and long term. 22-day betas are more sensitive and have a wider range of volatility (~0.4-1.8), capturing short-term market sentiment, while 252-day betas are smoother (~1.2-2.3), reflecting the longer-term trend. 22-day and 252-day betas were 1.8 and 1.5 at the end of 2023, respectively. At the end of 2023, the 22-day and 252-day betas will be 1.8 and 2.3, respectively, in line with the long-term trend analysis component of the AI. The point of calculating these two windows separately is to fully reveal Tesla's risk profile on different time scales, while meeting the needs of both long-term investment and short-term trading.")
st.divider()

st.markdown("### ACCURACY TEST (3): OPTIMAL PORTFOLIO")
st.image("assets/validation 7.png")
st.image("assets/validation 8.png")
st.markdown("""
| Performance | Code | Benjamin.AI |
|------------|------|------------|
| Annual Return | 9.40% | 3.23% |
| Annual Volatility | 11.50% | 11.54% |
| Sharpe Ratio | 0.68 | 0.28 |""")
st.markdown("""In the third test, we use data from four funds (SPy, TLT and GLD and MCHl) from 2015-01-01 to 2024.12-31 to construct the optimal portfolio. As shown on the left, in the Python computed results, we can see that the optimal portfolio represented by the blue line basically outperforms the equally weighted benchmark portfolio. However, in Benjamin AI's calculations, the optimal portfolio does not even perform as well as the benchmark portfolio. This is against common sense, if the optimal portfolio is not even as good as the basic equal-weighted portfolio, then it cannot be considered as the optimal portfolio, so Benjamin AI fails this validation.""")