import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Projects - Festus Bombo", page_icon="🚀", layout="wide")

# Custom CSS for dark mode
st.markdown("""
<style>
    .project-card {
        background: linear-gradient(135deg, #2a2a3e 0%, #1e1e2e 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        border-left: 5px solid #00d4aa;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(0, 212, 170, 0.3);
        transition: all 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 35px rgba(0, 212, 170, 0.25);
        border: 1px solid rgba(0, 212, 170, 0.5);
    }
    .project-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #00d4aa;
        margin-bottom: 1rem;
        text-shadow: 0 0 10px rgba(0, 212, 170, 0.3);
    }
    .project-description {
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        color: #fafafa;
        opacity: 0.9;
    }
    .tech-stack {
        margin: 1rem 0;
    }
    .tech-badge {
        background: linear-gradient(45deg, #00d4aa, #00b894);
        color: #0e1117;
        padding: 0.4rem 1rem;
        border-radius: 25px;
        margin: 0.3rem 0.3rem 0.3rem 0;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: bold;
        box-shadow: 0 3px 10px rgba(0, 212, 170, 0.3);
    }
    .project-stats {
        background: rgba(0, 212, 170, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
        border: 1px solid rgba(0, 212, 170, 0.2);
    }
    .stat-item {
        display: inline-block;
        margin: 0.5rem 1rem 0.5rem 0;
        color: #00d4aa;
        font-weight: bold;
    }
    .section-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00d4aa;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 0 0 15px rgba(0, 212, 170, 0.4);
    }
    .achievement-badge {
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
        box-shadow: 0 2px 8px rgba(255, 107, 107, 0.3);
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="section-header">🚀 Project Portfolio</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Project Overview Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Projects",
            value="15+",
            delta="Active Portfolio"
        )
    
    with col2:
        st.metric(
            label="Client Satisfaction",
            value="98%",
            delta="5-star ratings"
        )
    
    with col3:
        st.metric(
            label="Industries Served",
            value="8",
            delta="Diverse domains"
        )
    
    with col4:
        st.metric(
            label="ROI Generated",
            value="$2M+",
            delta="Client value"
        )
    
    # Featured Projects
    st.markdown("## 🎯 Featured Projects")
    
    # Project 1: Customer Segmentation
    st.markdown("""
    <div class="project-card">
        <div class="project-header">📊 Advanced Customer Segmentation Analysis</div>
        <div class="project-description">
        Developed a comprehensive customer segmentation solution for a major e-commerce platform with 500K+ customers. 
        Implemented RFM analysis, K-means clustering, and behavioral analytics to identify distinct customer segments, 
        resulting in a 25% increase in targeted marketing campaign effectiveness and 18% boost in customer retention.
        </div>
        
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Scikit-learn</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">Tableau</span>
            <span class="tech-badge">SQL</span>
            <span class="tech-badge">AWS</span>
        </div>
        
        <div class="project-stats">
            <span class="stat-item">🎯 25% ↑ Marketing ROI</span>
            <span class="stat-item">👥 500K+ Customers Analyzed</span>
            <span class="stat-item">📈 18% ↑ Retention Rate</span>
            <span class="stat-item">⏱️ 6 weeks delivery</span>
        </div>
        
        <div style="margin-top: 1rem;">
            <span class="achievement-badge">Client Choice Award</span>
            <span class="achievement-badge">5-Star Rating</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 2: Sales Forecasting
    st.markdown("""
    <div class="project-card">
        <div class="project-header">🤖 Intelligent Sales Forecasting System</div>
        <div class="project-description">
        Built an advanced time series forecasting model for a retail chain with 200+ stores. Combined ARIMA, 
        Random Forest, and LSTM neural networks to predict monthly sales with 92% accuracy. Integrated external 
        factors like seasonality, promotions, and economic indicators to optimize inventory management and reduce 
        stockouts by 35%.
        </div>
        
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">TensorFlow</span>
            <span class="tech-badge">Time Series</span>
            <span class="tech-badge">Power BI</span>
            <span class="tech-badge">Azure ML</span>
            <span class="tech-badge">LSTM</span>
        </div>
        
        <div class="project-stats">
            <span class="stat-item">🎯 92% Accuracy</span>
            <span class="stat-item">🏪 200+ Stores</span>
            <span class="stat-item">📉 35% ↓ Stockouts</span>
            <span class="stat-item">💰 $500K+ Savings</span>
        </div>
        
        <div style="margin-top: 1rem;">
            <span class="achievement-badge">Top Rated Plus</span>
            <span class="achievement-badge">Repeat Client</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3: Financial Risk Assessment
    st.markdown("""
    <div class="project-card">
        <div class="project-header">📈 Credit Risk Assessment Model</div>
        <div class="project-description">
        Developed a sophisticated credit risk assessment system for a fintech startup processing 10K+ loan 
        applications monthly. Implemented ensemble methods (XGBoost, Random Forest) with feature engineering 
        to achieve 88% accuracy in predicting loan defaults. Reduced manual review time by 60% while maintaining 
        strict risk thresholds.
        </div>
        
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">XGBoost</span>
            <span class="tech-badge">SQL</span>
            <span class="tech-badge">Docker</span>
            <span class="tech-badge">FastAPI</span>
            <span class="tech-badge">PostgreSQL</span>
        </div>
        
        <div class="project-stats">
            <span class="stat-item">🎯 88% Accuracy</span>
            <span class="stat-item">📋 10K+ Applications/month</span>
            <span class="stat-item">⚡ 60% ↓ Review Time</span>
            <span class="stat-item">🛡️ 15% ↓ Default Rate</span>
        </div>
        
        <div style="margin-top: 1rem;">
            <span class="achievement-badge">Industry Recognition</span>
            <span class="achievement-badge">Long-term Contract</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 4: Market Analysis Dashboard
    st.markdown("""
    <div class="project-card">
        <div class="project-header">🔍 Real-time Market Intelligence Dashboard</div>
        <div class="project-description">
        Created an automated market analysis platform that scrapes competitor data, social media sentiment, 
        and market trends in real-time. Built interactive dashboards with drill-down capabilities providing 
        strategic insights for C-level executives. Enabled data-driven decision making that increased market 
        share by 12% within 6 months.
        </div>
        
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Plotly Dash</span>
            <span class="tech-badge">Web Scraping</span>
            <span class="tech-badge">Sentiment Analysis</span>
            <span class="tech-badge">MongoDB</span>
            <span class="tech-badge">Redis</span>
        </div>
        
        <div class="project-stats">
            <span class="stat-item">📊 Real-time Updates</span>
            <span class="stat-item">🌐 50+ Data Sources</span>
            <span class="stat-item">📈 12% ↑ Market Share</span>
            <span class="stat-item">👥 C-level Adoption</span>
        </div>
        
        <div style="margin-top: 1rem;">
            <span class="achievement-badge">Innovation Award</span>
            <span class="achievement-badge">Executive Testimonial</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional Projects Summary
    st.markdown("## 📂 Additional Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        additional_projects = [
            {"name": "Healthcare Analytics Platform", "domain": "Healthcare", "impact": "30% efficiency gain"},
            {"name": "Supply Chain Optimization", "domain": "Logistics", "impact": "22% cost reduction"},
            {"name": "Social Media Analytics", "domain": "Marketing", "impact": "40% engagement boost"},
            {"name": "Fraud Detection System", "domain": "Fintech", "impact": "95% fraud detection"},
            {"name": "Energy Consumption Predictor", "domain": "Utilities", "impact": "15% energy savings"}
        ]
        
        for project in additional_projects:
            st.markdown(f"""
            <div style="background: rgba(0, 212, 170, 0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 3px solid #00d4aa;">
                <strong style="color: #00d4aa;">{project['name']}</strong><br>
                <small style="color: #fafafa; opacity: 0.8;">{project['domain']} • {project['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        more_projects = [
            {"name": "Recommendation Engine", "domain": "E-commerce", "impact": "28% sales increase"},
            {"name": "Predictive Maintenance", "domain": "Manufacturing", "impact": "45% downtime reduction"},
            {"name": "Price Optimization Model", "domain": "Retail", "impact": "12% profit margin"},
            {"name": "Churn Prediction Model", "domain": "Telecom", "impact": "20% retention boost"},
            {"name": "Inventory Optimization", "domain": "Supply Chain", "impact": "25% cost savings"}
        ]
        
        for project in more_projects:
            st.markdown(f"""
            <div style="background: rgba(0, 212, 170, 0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 3px solid #00d4aa;">
                <strong style="color: #00d4aa;">{project['name']}</strong><br>
                <small style="color: #fafafa; opacity: 0.8;">{project['domain']} • {project['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Technologies & Tools Used
    st.markdown("## 🛠️ Technology Stack Across Projects")
    
    tech_usage = {
        'Technology': ['Python', 'SQL', 'Tableau', 'Power BI', 'Scikit-learn', 'TensorFlow', 
                      'XGBoost', 'Pandas', 'NumPy', 'Plotly', 'AWS', 'Azure'],
        'Projects': [15, 12, 8, 6, 10, 5, 7, 15, 14, 9, 4, 3],
        'Proficiency': [95, 88, 85, 80, 90, 75, 85, 95, 92, 88, 70, 65]
    }
    
    df_tech = pd.DataFrame(tech_usage)
    
    fig = px.scatter(df_tech, x='Projects', y='Proficiency', size='Projects', 
                     hover_name='Technology', title="Technology Usage vs Proficiency",
                     color='Proficiency', color_continuous_scale='Viridis')
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#fafafa'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Project Impact Summary
    st.markdown("## 📊 Project Impact Summary")
    
    impact_data = {
        'Metric': ['Revenue Generated', 'Cost Savings', 'Efficiency Gains', 'Accuracy Improvements'],
        'Average Impact': [25, 30, 35, 15],
        'Best Result': [40, 60, 45, 25]
    }
    
    df_impact = pd.DataFrame(impact_data)
    
    fig_impact = px.bar(df_impact, x='Metric', y=['Average Impact', 'Best Result'],
                       title="Project Impact Metrics (%)",
                       barmode='group')
    
    fig_impact.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#fafafa'
    )
    
    st.plotly_chart(fig_impact, use_container_width=True)

if __name__ == "__main__":
    main()