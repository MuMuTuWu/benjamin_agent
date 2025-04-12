import streamlit as st

st.markdown("<h1 style='text-align: center;'>Upgrade your plan</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.html("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upgrade your plan</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }
        
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 0;
            background-color: #fff;
            overflow-x: hidden;
            width: 100%;
            min-height: 100vh;
        }
        
        h1 {
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 30px;
            color: #000;
        }
        
        .tab-container {
            display: flex;
            background-color: #f0f0f0;
            border-radius: 30px;
            padding: 5px;
            margin-bottom: 30px;
            width: 220px;
        }
        
        .tab {
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            text-align: center;
            font-size: 14px;
            font-weight: 500;
        }
        
        .tab.active {
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .plans-container {
            display: flex;
            justify-content: center;
            width: 100%;
            max-width: 100%;
            padding: 0 20px;
        }
        
        .plan-card {
            flex: 1;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 30px;
            position: relative;
            margin: 0 10px;
            min-width: 300px;
        }
        
        .plan-card.popular {
            background-color: #f5fbf7;
            border: 1px solid #e0f0e5;
        }
        
        .popular-tag {
            position: absolute;
            top: -10px;
            right: 20px;
            background-color: #00c853;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .plan-name {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 20px;
        }
        
        .price-container {
            display: flex;
            align-items: baseline;
            margin-bottom: 15px;
        }
        
        .currency {
            font-size: 20px;
            font-weight: 500;
        }
        
        .price {
            font-size: 48px;
            font-weight: 700;
            line-height: 1;
        }
        
        .period {
            font-size: 14px;
            color: #666;
            margin-left: 5px;
        }
        
        .plan-description {
            font-size: 16px;
            line-height: 1.5;
            color: #333;
            margin-bottom: 25px;
            min-height: 70px;
        }
        
        .btn {
            display: block;
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 25px;
            border: none;
        }
        
        .btn-primary {
            background-color: #00a040;
            color: white;
        }
        
        .btn-dark {
            background-color: #000;
            color: white;
        }
        
        .btn-light {
            background-color: #f0f0f0;
            color: #333;
        }
        
        .features-list {
            list-style-type: none;
        }
        
        .feature-item {
            display: flex;
            margin-bottom: 15px;
            font-size: 14px;
            line-height: 1.4;
        }
        
        .feature-item:before {
            content: "✓";
            color: #00a040;
            margin-right: 10px;
            font-weight: bold;
        }
        
        .limits-text {
            font-size: 12px;
            color: #666;
            margin-top: 20px;
        }
        
        .footer-text {
            font-size: 12px;
            color: #666;
            margin-top: 30px;
        }
        
        .footer-text a {
            color: #666;
            text-decoration: underline;
        }
        
        @media (max-width: 1024px) {
            .plans-container {
                flex-direction: column;
                align-items: center;
            }
            
            .plan-card {
                width: 100%;
                max-width: 500px;
                margin-bottom: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="plans-container">
        <!-- Free Plan -->
        <div class="plan-card">
            <h2 class="plan-name">Free</h2>
            <div class="price-container">
                <span class="currency">$</span>
                <span class="price">0</span>
                <span class="period">USD/month</span>
            </div>
            <p class="plan-description">Explore how Benjamin.AI can help you with everyday financial tasks</p>
            <button class="btn btn-light">Your current plan</button>
            
            <ul class="features-list">
                <li class="feature-item">Access to basic models include GPT-4o mini, Claude 3.5 Haiku, etc.</li>
                <li class="feature-item">Limited access to advanced models include GPT-4o, Claude 3.7, Grok 3, etc.</li>
                <li class="feature-item">Real-time data from the web with search</li>
                <li class="feature-item">Limited access to file uploads, and advanced data analysis</li>
                <li class="feature-item">Limited access to Benjamin Agents.</li>         
            </ul>
            
            <div class="footer-text">
                Have an existing plan? See <a href="#">billing help</a>
            </div>
        </div>
        
        <!-- Plus Plan -->
        <div class="plan-card popular">
            <div class="popular-tag">POPULAR</div>
            <h2 class="plan-name">Plus</h2>
            <div class="price-container">
                <span class="currency">$</span>
                <span class="price">20</span>
                <span class="period">USD/month</span>
            </div>
            <p class="plan-description">Level up investment analytics, portfolio construction and strategy development</p>
            <button class="btn btn-primary">Get Plus</button>
            
            <ul class="features-list">
                <li class="feature-item">Everything in Free</li>
                <li class="feature-item">Extended access to advanced models include GPT-4o, Claude 3.7, Grok 3, etc.</li>
                <li class="feature-item">Extended limits on messaging, file uploads, and advanced data analysis</li>
                <li class="feature-item">Access to deep research, multiple reasoning models (o3-mini, o1, Claude 3.7 thinking, etc.)</li>
                <li class="feature-item">Extended access to Benjamin Agents.</li>
                <li class="feature-item">Limited access to Benjamin.AI Pro+, a general AI agent that solves complex tasks.</li>
            </ul>
            
            <div class="limits-text">Limits apply</div>
        </div>
        
        <!-- Pro Plan -->
        <div class="plan-card">
            <h2 class="plan-name">Pro</h2>
            <div class="price-container">
                <span class="currency">$</span>
                <span class="price">200</span>
                <span class="period">USD/month</span>
            </div>
            <p class="plan-description">Get the best of Benjamin.AI with the highest level of access</p>
            <button class="btn btn-dark">Get Pro</button>
            
            <ul class="features-list">
                <li class="feature-item">Everything in Plus</li>
                <li class="feature-item">Unlimited access to all advanced models and reasoning models</li>
                <li class="feature-item">Unlimited access on messaging, file uploads, and advanced data analysis</li>
                <li class="feature-item">Unlimited access to deep research</li>
                <li class="feature-item">Unlimited access to Benjamin Agents.</li>
                <li class="feature-item">Unlimited access to Benjamin.AI Pro+.</li>
            </ul>
            
            <div class="limits-text">Unlimited subject to abuse guardrails. <a href="#">Learn more</a></div>
        </div>
    </div>
    
    <script>
        // Simple tab switching functionality
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
            });
        });
    </script>
</body>
</html>""")