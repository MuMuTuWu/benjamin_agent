import streamlit as st

st.title("🎯 From Benjamin.AI to Benjamin.AI Pro+")

st.subheader("1. Adjust the conversation entry to improve the UX")
st.markdown("Provide different AI - Agent entrances so that users can choose the appropriate Agent according to their needs.")
st.markdown("**Current Layout:**")
st.image("assets/improvement 1.png")
st.markdown("**Improved Layout:**")
st.html("""<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>精致卡片布局</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      background-color: #f0f2f5;
      padding: 30px;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    
    .card-container {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      justify-content: center;
      max-width: 1200px;
    }
    
    .card {
      background-color: white;
      border-radius: 8px;
      padding: 8px 6px;
      width: 150px;
      height: 85px;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }
    
    .card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--start-color), var(--end-color));
    }
    
    .card:nth-child(1) {
      --start-color: #3498db;
      --end-color: #2980b9;
    }
    
    .card:nth-child(2) {
      --start-color: #2ecc71;
      --end-color: #27ae60;
    }
    
    .card:nth-child(3) {
      --start-color: #e74c3c;
      --end-color: #c0392b;
    }
    
    .card:nth-child(4) {
      --start-color: #f39c12;
      --end-color: #e67e22;
    }
    
    .card:nth-child(5) {
      --start-color: #9b59b6;
      --end-color: #8e44ad;
    }
    
    .card:nth-child(6) {
      --start-color: #1abc9c;
      --end-color: #16a085;
    }
    
    .card:nth-child(7) {
      --start-color: #e67e22;
      --end-color: #d35400;
    }
    
    .card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
    }
    
    .card:hover::after {
      opacity: 1;
    }
    
    .card::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(0deg, rgba(var(--rgb-color), 0.05) 0%, rgba(255,255,255,0) 40%);
      opacity: 0;
      transition: opacity 0.25s ease;
    }
    
    .card:nth-child(1) { --rgb-color: 52, 152, 219; }
    .card:nth-child(2) { --rgb-color: 46, 204, 113; }
    .card:nth-child(3) { --rgb-color: 231, 76, 60; }
    .card:nth-child(4) { --rgb-color: 243, 156, 18; }
    .card:nth-child(5) { --rgb-color: 155, 89, 182; }
    .card:nth-child(6) { --rgb-color: 26, 188, 156; }
    .card:nth-child(7) { --rgb-color: 230, 126, 34; }
    
    .card-title {
      color: #2d3436;
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      font-weight: 600;
      line-height: 1.1;
      letter-spacing: -0.2px;
      padding: 0;
      margin: 0;
    }
  </style>
</head>
<body>
  <div class="card-container">
    <div class="card">
      <h3 class="card-title">Asset Data Analysis</h3>
    </div>
    <div class="card">
      <h3 class="card-title">Strategy Backtest</h3>
    </div>
    <div class="card">
      <h3 class="card-title">Portfolio Optimisation</h3>
    </div>
    <div class="card">
      <h3 class="card-title">Macro Data Analysis</h3>
    </div>
    <div class="card">
      <h3 class="card-title">Merged Data Analysis</h3>
    </div>
    <div class="card">
      <h3 class="card-title">SEC Filings</h3>
    </div>
    <div class="card">
      <h3 class="card-title">Swift Data Analysis</h3>
    </div>
  </div>
</body>
</html>""")
st.html("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LLM Input Box</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f5f5f5;
    }
    
    .input-container {
      display: flex;
      width: 100%;
      background-color: white;
      padding: 15px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      box-sizing: border-box;
    }
    
    .message-input {
      flex: 1;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      padding: 12px;
      font-size: 16px;
      resize: none;
      min-height: 24px;
      max-height: 120px;
      outline: none;
      transition: border-color 0.3s;
    }
    
    .message-input:focus {
      border-color: #2b6cb0;
    }
    
    .send-button {
      margin-left: 10px;
      background-color: #2b6cb0;
      color: white;
      border: none;
      border-radius: 8px;
      padding: 0 20px;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s;
      white-space: nowrap;
    }
    
    .send-button:hover {
      background-color: #1a4971;
    }
  </style>
</head>
<body>
  <div class="input-container">
    <textarea 
      class="message-input" 
      id="messageInput" 
      placeholder="Enter your question..." 
      rows="1"></textarea>
    <button class="send-button" id="sendButton">Send</button>
  </div>
  
  <script>
    const messageInput = document.getElementById('messageInput');
    
    // Auto-adjust textarea height
    messageInput.addEventListener('input', function() {
      this.style.height = 'auto';
      this.style.height = (this.scrollHeight) + 'px';
    });
  </script>
</body>
</html>""")
st.divider()


st.subheader("2. Improve the existing functions and develop the agent workflow.")
st.markdown("Hire a better person to develop more tools and improve their Agent workflows.")

st.subheader("3. DeepResearch functionality")
st.markdown("Offer comprehensive research reports like DeepResearch products offered by ChatGPT, Gemini, Perplexity, etc.")

# 创建三列布局展示DeepResearch相关图片
col1, col2, col3 = st.columns(3)
with col1:
    st.image("assets/improvement 2.png")
with col2:
    st.image("assets/improvement 3.png")
with col3:
    st.image("assets/improvement 4.png")

st.subheader("4. General AI-Agent")
st.markdown("Solve long-tail problems that the workflow agent cannot handle.")
st.image("assets/improvement 5.png")