# Benjamin.AI

<img src="assets/artificial-bot-intelligence-svgrepo-com.svg" width="80" align="left" style="margin-right: 15px"/>

Benjamin AI 是一个专注于量化金融的智能技术平台，致力于为投资者和机构提供先进的金融分析工具和解决方案。该平台利用前沿人工智能技术和数据驱动方法，覆盖投资组合管理、风险评估、交易策略开发、宏观经济分析和股票估值等领域。

## 项目概述

Benjamin.AI 是一个基于 Streamlit 构建的金融分析平台，集成了多种 AI 代理功能，可以执行 SQL 查询、数据分析和金融建模等任务。该项目利用 LangChain 框架和 DeepSeek 大语言模型，结合 ClickHouse 数据库，为用户提供强大的金融数据分析能力。

## 项目结构

```
.
├── agent/                  # 核心代理功能模块
│   ├── __init__.py        # 初始化文件
│   ├── llm.py             # 语言模型配置
│   ├── prompt.py          # 提示词模板
│   └── tool.py            # 工具函数（SQL执行、数据处理等）
├── pages_agent/           # 代理页面
│   ├── 1_sql_agent.py     # SQL数据分析代理
│   └── 2_benjamin_pro.py  # Benjamin.AI专业版
├── pages_blog/            # 博客页面
│   ├── 1_introduction.py  # 项目介绍
│   ├── 2_capability_validation.py # 能力验证
│   ├── 3_agentic_view.py  # 代理视图
│   ├── 4_pricing.py       # 价格信息
│   └── agent_demo_response.py # 代理演示响应
├── assets/                # 静态资源（图片等）
├── .streamlit/            # Streamlit配置
├── app.py                 # 主应用入口
└── requirements.txt       # 项目依赖
```

## 核心功能

- **SQL数据分析代理**：通过自然语言与SQL数据库交互，执行查询并生成数据摘要
- **Python代码执行**：支持在应用内执行Python代码进行数据分析和可视化
- **ClickHouse数据库集成**：连接高性能的ClickHouse数据库进行金融数据查询
- **数据可视化**：自动生成数据统计摘要和可视化图表
- **投资组合优化**：使用PyPortfolioOpt进行资产配置优化

## 安装与运行

### 环境要求

- Python 3.8+
- ClickHouse数据库访问权限
- DeepSeek API密钥

### 安装步骤

1. 克隆项目仓库

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 创建`.env`文件并配置以下环境变量：
```
CLICKHOUSE_PASSWORD=your_password
OPENAI_API_KEY=your_deepseek_api_key
```

4. 运行应用
```bash
streamlit run app.py
```

5. 在浏览器中访问应用（默认地址：http://localhost:8501）

## 使用说明

1. 在侧边栏输入ClickHouse密码和DeepSeek API密钥
2. 导航到「SQL Data Analysis Agent」页面使用SQL查询功能
3. 通过自然语言描述您的数据分析需求
4. 查看生成的SQL查询、数据摘要和分析结果

## 技术栈

- **前端框架**：Streamlit
- **AI框架**：LangChain、LangGraph
- **语言模型**：DeepSeek
- **数据库**：ClickHouse
- **数据分析**：Pandas、PyPortfolioOpt
- **环境配置**：python-dotenv