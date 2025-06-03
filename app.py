import streamlit as st
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Festus Matsitsa Bombo - Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        color: #1f77b4;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .contact-info {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def create_download_link():
    """Create a download link for the resume PDF"""
    try:
        with open("attached_assets/My Resume.pdf", "rb") as file:
            pdf_data = file.read()
            b64 = base64.b64encode(pdf_data).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="Festus_Bombo_Resume.pdf">📄 Download Resume (PDF)</a>'
            return href
    except FileNotFoundError:
        return '<p>Resume file not available for download</p>'

def main():
    # Header
    st.markdown('<h1 class="main-header">FESTUS MATSITSA BOMBO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">DATA SCIENTIST</p>', unsafe_allow_html=True)
    
    # Navigation info
    st.sidebar.title("🧭 Navigation")
    st.sidebar.info("Use the pages in the sidebar to explore different sections of the portfolio.")
    
    # Resume download
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📄 Resume")
    st.sidebar.markdown(create_download_link(), unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="section-header">👨‍💻 About Me</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
        <p>Passionate Data Scientist with a strong background in data analysis, machine learning, 
        data visualization, and statistical modeling. I specialize in transforming complex datasets 
        into actionable insights that support data-driven decision-making and drive business success.</p>
        
        <p>Proficient in Python, R, SQL, Excel, Power BI, and Tableau, with hands-on experience 
        using libraries such as Pandas, NumPy, Scikit-learn, and TensorFlow. Experienced in 
        developing predictive models, performing exploratory data analysis (EDA), A/B testing, 
        data cleaning, and applying advanced statistical methods to solve real-world problems.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h2 class="section-header">🎯 Core Competencies</h2>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
            **Technical Skills:**
            - 🐍 Python & R Programming
            - 📊 Data Visualization (Tableau, Power BI)
            - 🤖 Machine Learning & Deep Learning
            - 📈 Statistical Analysis & Modeling
            - 🗄️ SQL & Database Management
            """)
        
        with col_b:
            st.markdown("""
            **Soft Skills:**
            - 🧠 Analytical Thinking
            - 🔍 Attention to Detail
            - 🗣️ Communication & Collaboration
            - ⚡ Adaptability & Innovation
            - 📋 Project Management
            """)
    
    with col2:
        st.markdown('<h2 class="section-header">📞 Contact</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="contact-info">
        <p><strong>🏫 Education:</strong><br>
        BSc Computer Science<br>
        Pwani University<br>
        Aug 2022 - Sep 2027</p>
        
        <p><strong>💼 Current Status:</strong><br>
        Freelance Data Scientist<br>
        Fiverr & Upwork</p>
        
        <p><strong>🌟 Experience:</strong><br>
        3+ years in Data Science<br>
        Specialized in client solutions</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent Projects Section
    st.markdown('<h2 class="section-header">🚀 Featured Capabilities</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4>📊 Data Analysis</h4>
        <p>Comprehensive EDA, statistical analysis, and data preprocessing for actionable insights.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4>🤖 Machine Learning</h4>
        <p>Predictive modeling, classification, regression, and advanced ML algorithm implementation.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-box">
        <h4>📈 Visualization</h4>
        <p>Interactive dashboards, custom charts, and compelling data storytelling solutions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("---")
    st.markdown("### 🔧 Explore My Data Science Toolkit")
    st.info("Navigate to the **Data Science Toolkit** page to see interactive tools for data analysis, visualization, and machine learning!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
    <p>© 2024 Festus Matsitsa Bombo | Data Scientist Portfolio</p>
    <p>Committed to continuous learning, innovation, and delivering high-impact, scalable analytical solutions.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
