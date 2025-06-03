import streamlit as st
import datetime
import json
import os

st.set_page_config(page_title="Contact Me - Festus Bombo", page_icon="📨", layout="wide")

# Custom CSS for dark mode
st.markdown("""
<style>
    .contact-form {
        background: linear-gradient(135deg, #2a2a3e 0%, #1e1e2e 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        border-left: 5px solid #00d4aa;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(0, 212, 170, 0.3);
    }
    .contact-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00d4aa;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 0 0 15px rgba(0, 212, 170, 0.4);
    }
    .contact-info-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 2px solid rgba(0, 212, 170, 0.3);
        box-shadow: 0 8px 30px rgba(0, 212, 170, 0.1);
    }
    .contact-method {
        background: rgba(0, 212, 170, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 3px solid #00d4aa;
        transition: all 0.3s ease;
    }
    .contact-method:hover {
        background: rgba(0, 212, 170, 0.2);
        transform: translateX(5px);
    }
    .email-link {
        color: #00d4aa;
        text-decoration: none;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border: 2px solid #00d4aa;
        border-radius: 25px;
        display: inline-block;
        transition: all 0.3s ease;
        background: rgba(0, 212, 170, 0.1);
        margin: 0.5rem;
    }
    .email-link:hover {
        background: #00d4aa;
        color: #0e1117;
        transform: scale(1.05);
    }
    .message-preview {
        background: rgba(0, 212, 170, 0.05);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid rgba(0, 212, 170, 0.2);
    }
</style>
""", unsafe_allow_html=True)

def save_message(name, email, phone, subject, message, message_type):
    """Save message to a local file"""
    try:
        message_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "name": name,
            "email": email,
            "phone": phone,
            "subject": subject,
            "message": message,
            "type": message_type
        }
        
        # Create messages directory if it doesn't exist
        if not os.path.exists("messages"):
            os.makedirs("messages")
        
        # Save to JSON file
        filename = f"messages/message_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(message_data, f, indent=2)
        
        return True
    except Exception as e:
        st.error(f"Error saving message: {e}")
        return False

def main():
    st.markdown('<h1 class="contact-header">📨 Get In Touch</h1>', unsafe_allow_html=True)
    
    # Contact Information Section
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info-card">
            <h3 style="color: #00d4aa; margin-bottom: 1.5rem; text-align: center;">📞 Contact Information</h3>
            
            <div class="contact-method">
                <h4 style="color: #00d4aa; margin-bottom: 0.5rem;">📧 Email</h4>
                <p style="margin: 0; color: #fafafa;">bombomatsitsa@gmail.com</p>
            </div>
            
            <div class="contact-method">
                <h4 style="color: #00d4aa; margin-bottom: 0.5rem;">📱 Phone</h4>
                <p style="margin: 0; color: #fafafa;">+254 702 816 978</p>
            </div>
            
            <div class="contact-method">
                <h4 style="color: #00d4aa; margin-bottom: 0.5rem;">🔗 GitHub</h4>
                <p style="margin: 0; color: #fafafa;">
                    <a href="https://github.com/Bombo9" target="_blank" style="color: #00d4aa;">github.com/Bombo9</a>
                </p>
            </div>
            
            <div class="contact-method">
                <h4 style="color: #00d4aa; margin-bottom: 0.5rem;">🎓 Education</h4>
                <p style="margin: 0; color: #fafafa;">BSc Computer Science</p>
                <p style="margin: 0; color: #fafafa; opacity: 0.8;">Pwani University (2022-2027)</p>
            </div>
            
            <div style="text-align: center; margin-top: 2rem;">
                <a href="mailto:bombomatsitsa@gmail.com" class="email-link">
                    📧 Send Email
                </a>
                <a href="tel:+254702816978" class="email-link">
                    📱 Call Now
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-form">
            <h3 style="color: #00d4aa; margin-bottom: 1.5rem; text-align: center;">💌 Send Me a Message</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact Form
        with st.form("contact_form", clear_on_submit=True):
            # Personal Information
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Your Name *", placeholder="Enter your full name")
            with col_b:
                email = st.text_input("Email Address *", placeholder="your.email@example.com")
            
            phone = st.text_input("Phone Number (Optional)", placeholder="+1234567890")
            
            # Message Type
            message_type = st.selectbox("Message Type", [
                "General Inquiry",
                "Job Opportunity",
                "Internship Opportunity",
                "Freelance Project",
                "Collaboration Request",
                "Technical Question",
                "Other"
            ])
            
            subject = st.text_input("Subject *", placeholder="Brief subject of your message")
            
            message = st.text_area("Your Message *", 
                                 placeholder="Please describe your inquiry, project requirements, or any questions you have. I'll get back to you as soon as possible!",
                                 height=150)
            
            # Availability preferences
            st.write("**Preferred Contact Method:**")
            contact_prefs = st.multiselect("Select all that apply:", [
                "Email",
                "Phone Call",
                "WhatsApp",
                "Video Call (Zoom/Teams)"
            ])
            
            # Urgency
            urgency = st.radio("Urgency Level:", [
                "Low - Response within a week",
                "Medium - Response within 2-3 days", 
                "High - Response within 24 hours"
            ])
            
            submitted = st.form_submit_button("Send Message 🚀", use_container_width=True)
            
            if submitted:
                if name and email and subject and message:
                    # Save the message
                    if save_message(name, email, phone, subject, message, message_type):
                        st.success("✅ Message sent successfully! I'll get back to you soon.")
                        
                        # Show message preview
                        st.markdown("""
                        <div class="message-preview">
                            <h4 style="color: #00d4aa;">Message Preview:</h4>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.write(f"**From:** {name} ({email})")
                        if phone:
                            st.write(f"**Phone:** {phone}")
                        st.write(f"**Type:** {message_type}")
                        st.write(f"**Subject:** {subject}")
                        st.write(f"**Message:** {message}")
                        st.write(f"**Urgency:** {urgency}")
                        if contact_prefs:
                            st.write(f"**Preferred Contact:** {', '.join(contact_prefs)}")
                        
                        st.info("💡 You can also reach me directly via email or phone for faster response!")
                    else:
                        st.error("❌ Sorry, there was an error sending your message. Please try again or contact me directly.")
                else:
                    st.warning("⚠️ Please fill in all required fields (marked with *)")
    
    # Additional Information
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-method">
            <h4 style="color: #00d4aa;">🕒 Response Time</h4>
            <p style="color: #fafafa;">I typically respond within 24 hours during weekdays</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-method">
            <h4 style="color: #00d4aa;">🌍 Availability</h4>
            <p style="color: #fafafa;">Open to remote work and international opportunities</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-method">
            <h4 style="color: #00d4aa;">💼 Services</h4>
            <p style="color: #fafafa;">Data analysis, ML models, dashboards, consulting</p>
        </div>
        """, unsafe_allow_html=True)
    
    # FAQ Section
    st.markdown("## ❓ Frequently Asked Questions")
    
    with st.expander("What types of projects do you work on?"):
        st.write("""
        I specialize in:
        - **Data Analysis & Visualization**: EDA, statistical analysis, interactive dashboards
        - **Machine Learning**: Predictive models, classification, regression, clustering
        - **Business Intelligence**: KPI tracking, performance analytics, reporting
        - **Data Engineering**: Data cleaning, preprocessing, pipeline development
        - **Consulting**: Data strategy, technology recommendations, training
        """)
    
    with st.expander("What is your typical project timeline?"):
        st.write("""
        Project timelines vary based on complexity:
        - **Simple Analysis**: 1-3 days
        - **Dashboard Development**: 3-7 days  
        - **ML Model Development**: 1-3 weeks
        - **Complex Analytics Projects**: 2-8 weeks
        
        I provide detailed project timelines during initial consultation.
        """)
    
    with st.expander("Do you offer ongoing support?"):
        st.write("""
        Yes! I provide:
        - **Post-delivery support**: Bug fixes and minor adjustments
        - **Maintenance contracts**: Regular updates and monitoring
        - **Training sessions**: Team training on delivered solutions
        - **Consulting retainers**: Ongoing advisory services
        """)
    
    with st.expander("What are your rates?"):
        st.write("""
        My rates are competitive and depend on:
        - Project complexity and scope
        - Timeline requirements
        - Technology stack needed
        - Level of support required
        
        I offer both fixed-price and hourly arrangements. Contact me for a customized quote!
        """)

if __name__ == "__main__":
    main()