import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
from langchain.memory import ConversationBufferMemory

# 定义工具函数
@tool
def search_knowledge_base(query: str) -> str:
    """搜索知识库以回答用户的问题"""
    # 这里可以连接到实际的知识库，现在我们返回一个模拟的回答
    knowledge = {
        "人工智能": "人工智能(AI)是计算机科学的一个分支，致力于创建能够模拟人类智能的系统。",
        "机器学习": "机器学习是人工智能的一个子领域，专注于开发能够从数据中学习的算法。",
        "深度学习": "深度学习是机器学习的一个子领域，使用神经网络进行学习。",
        "自然语言处理": "自然语言处理(NLP)是AI的一个分支，专注于使计算机能够理解和处理人类语言。",
        "LangChain": "LangChain是一个用于构建基于大型语言模型的应用程序的框架，它提供了一系列工具和组件。"
    }
    
    for key, value in knowledge.items():
        if key.lower() in query.lower():
            return value
    
    return "抱歉，我的知识库中没有找到相关信息。"

@tool
def calculate(expression: str) -> str:
    """计算数学表达式"""
    try:
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

@tool
def get_current_weather(location: str) -> str:
    """获取指定位置的当前天气"""
    # 这里应该连接到实际的天气API，现在我们返回一个模拟的回答
    weather_data = {
        "北京": "晴天，温度25°C",
        "上海": "多云，温度28°C",
        "广州": "小雨，温度30°C",
        "深圳": "阴天，温度29°C",
        "香港": "晴天，温度27°C"
    }
    
    if location in weather_data:
        return f"{location}的当前天气: {weather_data[location]}"
    else:
        return f"抱歉，没有{location}的天气信息。"

# 创建Agent
def create_agent():
    # 初始化语言模型
    llm = ChatOpenAI(
        temperature=0.7,
        model="gpt-3.5-turbo",
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # 定义工具列表
    tools = [search_knowledge_base, calculate, get_current_weather]
    
    # 创建对话记忆
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # 创建提示模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是Benjamin AI，一个友好、专业的AI助手。你的目标是帮助用户解决问题，提供准确的信息，并在需要时使用工具来增强你的能力。"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # 创建agent
    agent = create_openai_functions_agent(llm, tools, prompt)
    
    # 创建agent执行器
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor

# 运行Agent
def run_agent(agent, query):
    try:
        response = agent.invoke({"input": query})
        return response["output"]
    except Exception as e:
        return f"发生错误: {str(e)}"