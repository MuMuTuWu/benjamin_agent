# Benjamin.AI

<img src="assets/artificial-bot-intelligence-svgrepo-com.svg" width="80" align="left" style="margin-right: 15px"/>

Benjamin AI is an intelligent technology platform specializing in quantitative finance, dedicated to providing investors and institutions with advanced financial analysis tools and solutions. The platform leverages cutting-edge artificial intelligence technologies and data-driven methods, covering areas such as portfolio management, risk assessment, trading strategy development, macroeconomic analysis, and stock valuation.

## Project Overview

Benjamin.AI is a financial analysis platform built on Streamlit, integrating various AI agent functionalities capable of executing SQL queries, data analysis, and financial modeling tasks. The project utilizes the LangChain framework and the DeepSeek large language model, combined with the ClickHouse database, to provide users with powerful financial data analysis capabilities.

## Core Features

- **SQL Data Analysis Agent**: Interact with SQL databases using natural language, execute queries, and generate data summaries
- **Python Code Execution**: Supports executing Python code within the application for data analysis and visualization
- **ClickHouse Database Integration**: Connects to the high-performance ClickHouse database for financial data queries
- **Data Visualization**: Automatically generates statistical summaries and visual charts
- **Portfolio Optimization**: Uses PyPortfolioOpt for asset allocation optimization

## Installation and Execution

### Requirements

- Python 3.8+
- ClickHouse database access
- DeepSeek API key

### Installation Steps

1. Clone the project repository

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and configure the following environment variables:
```
CLICKHOUSE_PASSWORD=your_password
OPENAI_API_KEY=your_deepseek_api_key
```

4. Run the application
```bash
streamlit run app.py
```

5. Access the application in your browser (default address: http://localhost:8501)

## Usage Instructions

1. Enter your ClickHouse password and DeepSeek API key in the sidebar
2. Navigate to the "SQL Data Analysis Agent" page to use the SQL query functionality
3. Describe your data analysis needs in natural language
4. View the generated SQL queries, data summaries, and analysis results

---