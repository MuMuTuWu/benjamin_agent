BENJAMIN_AI_CAPABILITY = """I can help you with a wide range of financial and investment topics. Here are my main areas of expertise:

**Investment Analysis**

- Stock, cryptocurrency, forex, and commodity analysis
- Technical and fundamental analysis
- Financial statement analysis
- Market sentiment and news monitoring
- Real-time market data and historical performance metrics

**Portfolio Management**

- Portfolio optimization and construction
- Asset allocation strategies
- Risk management
- Performance attribution
- Rebalancing strategies

**Trading Strategies**

- Strategy development and backtesting
- Technical indicator analysis
- Trading system evaluation
- Risk/reward optimization
- Performance benchmarking

**Economic Analysis**

- Macroeconomic indicators
- Interest rates and monetary policy
- Economic trends and forecasting
- Cross-market relationships
- Global economic developments

**Research & Education**

- Investment methodologies
- Risk management frameworks
- Market mechanics
- Portfolio theory
- Trading concepts

I can provide data-driven analysis, charts, performance metrics, and actionable insights across all these areas. Would you like to explore any particular topic in detail?"""


BENJAMIN_AI_TOOLS = """Let me create a clear markdown table summarizing all available tools and their key parameters.

Here's the reconstructed table in compact markdown format:

| Tool Name | Primary Purpose | Key Parameters | When to Use |
| --- | --- | --- | --- |
| Search | News and ticker search | `tool_input`: Search query | - Find correct asset tickers<br>- Get latest news and sentiment<br>- Verify symbols<br>- Get social media sentiment |
| Asset Data Analysis | Financial asset analysis | `input_str`: "symbol,start_date,end_date[,frequency][,financials]" | - Single asset analysis<br>- Asset relationships<br>- Multiple assets comparison<br>- Comprehensive stock reports |
| Strategy Backtest | Trading strategy testing | `input_str`: "symbol(s),start_date,end_date,strategy_type,strategy_direction,parameters" | - Test trading strategies<br>- Evaluate strategy performance<br>- Compare with benchmarks |
| Portfolio Optimisation | Portfolio construction | `input_str`: "symbols,start_date,end_date,lookback,model,optimization_objective,rebalancing_period[,weights]" | - Multi-asset portfolio construction<br>- Portfolio optimization<br>- Performance evaluation |
| Macro Data Analysis | Economic data analysis | `input_str`: "query,start_date,end_date[,frequency][,unrevised]" | - Economic indicators<br>- Interest rates<br>- Bond yields<br>- Credit spreads |
| Merged Data Analysis | Asset-macro relationships | `input_str`: "query,asset_symbols,start_date,end_date[,frequency][,unrevised]" | - Study relationships between:<br>• Macro data and assets<br>• Interest rates vs markets<br>• GDP vs asset prices |
| VectorStore | Research knowledge base | `query`: Research topic | - Portfolio management info<br>- Asset allocation research<br>- Risk management data<br>- Quantitative finance concepts |
| SEC Filings | Company filings analysis | `input`: "Query;Year(s);Ticker(s)" | - Analyze 10-K filings<br>- Company financials<br>- Risk factors<br>- Management discussion |
| Process File | File analysis | `output`: File content | - Process uploaded files<br>- Analyze file content<br>- Support for txt, docx, pdf, csv, xlsx |
| Swift Data Analysis | Quick data queries | `input_str`: "symbol(s),start_date,end_date,frequency,create_charts" | - Fast basic data queries<br>- Simple price/volume data<br>- Basic chart creation |

**Important Notes:**

- Default current date: 2025-03-17
- Default lookback period: 252 days
- Transaction costs assumption: 20bps
- Initial capital assumption: $10,000
- All date formats: YYYY-MM-DD
- Frequencies available: daily, weekly, monthly, quarterly, yearly

This table provides a high-level overview of each tool's primary purpose and key parameters. Each tool has specific use cases and limitations that should be considered when processing requests."""