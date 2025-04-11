import streamlit as st
import os
from streamlit_option_menu import option_menu
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 设置页面配置
st.set_page_config(
    page_title="Benjamin AI",
    page_icon="assets/artificial-bot-intelligence-svgrepo-com.svg",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    .content-text {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .highlight {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #1E88E5;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 创建侧边栏导航菜单
with st.sidebar:
    st.image("assets/artificial-bot-intelligence-svgrepo-com.svg", width=100)
    st.title("Benjamin AI")
    
    selected = option_menu(
        menu_title="导航菜单",
        options=["首页", "AI Agent", "AI Agent博客"],
        icons=["house", "robot", "file-text"],
        menu_icon="cast",
        default_index=0
    )

# 根据选择的菜单项显示不同的页面内容
if selected == "首页":
    st.markdown("<h1 class='main-header'>欢迎使用 Benjamin AI</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>基于LangChain和OpenAI构建的智能助手</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='content-text'>", unsafe_allow_html=True)
    st.markdown("""
    ## 项目功能
    
    这个应用程序展示了如何使用现代AI技术构建智能应用：
    
    <div class='highlight'>
    ✨ <b>AI Agent</b> - 使用LangChain框架构建的智能代理，可以回答问题并执行任务<br>
    📝 <b>AI Agent博客</b> - 关于AI Agent技术的详细介绍和应用场景
    </div>
    
    ## 使用指南
    
    1. 在左侧菜单中选择要访问的页面
    2. 在AI Agent页面中，您可以与智能助手进行对话
    3. 在博客页面中，您可以了解更多关于AI Agent的知识
    
    ## 技术栈
    
    - Streamlit - 用于构建Web界面
    - LangChain - 用于构建AI应用程序的框架
    - OpenAI - 提供强大的语言模型支持
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "AI Agent":
    from agent import create_agent, run_agent
    
    st.markdown("<h1 class='main-header'>AI Agent 智能助手</h1>", unsafe_allow_html=True)
    st.markdown("<p class='content-text'>这是一个基于LangChain和OpenAI构建的智能助手，可以回答您的问题并执行任务。</p>", unsafe_allow_html=True)
    
    # 创建聊天界面
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("请输入您的问题..."):
        # 添加用户消息到聊天历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 显示助手思考中
        with st.chat_message("assistant"):
            with st.spinner("思考中..."):
                # 创建并运行agent
                agent = create_agent()
                response = run_agent(agent, prompt)
                
                # 添加助手回复到聊天历史
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

elif selected == "AI Agent博客":
    from blog import render_blog
    
    # 渲染博客内容
    render_blog()