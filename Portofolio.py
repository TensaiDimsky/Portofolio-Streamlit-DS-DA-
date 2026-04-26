import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dimas Wibisono Portfolio",
    page_icon="📊",
    layout="wide"
)
df = pd.read_csv('shopping_cart.csv')
#--------------------------------------------------------------------------------------------------------------------------------------------
col1, col2 = st.columns([1, 3])
with col1:
    st.image('Foto profil.jpg', width=150)

with col2:
    st.title('HI! My Name Is Dimas Wibisono')
    st.subheader("Material Scientist Turned Data Scientist — Precision Meets Analytics")
#-------------------------------------------------------------------------------------------------------------------------------
st.title('**👤 About Me**')
st.write("""
        I’m a Jakarta-based **Data Analyst & Data Scientist** who turns raw data into clear, actionable stories. I thrive on the full analytics lifecycle — from writing efficient SQL queries to uncovering patterns with Python, and finally delivering insights through interactive dashboards.          
        """)
st.markdown("Recently, I graduated from the Full Stack Data Analyst & Data Science Bootcamp at Dibimbing.id, where I gained hands-on experience in data analysis, machine learning, and full-stack data science. I’m constantly sharpening my skills and looking for opportunities to drive real impact through data.")

col1, col2 = st.columns([1, 3]) 
with col1 :
    st.write("- 📧 **Email:**")
    st.markdown("- 💼 **LinkedIn:**")
    st.markdown("- 🐙 **GitHub:**")

with col2 :
    st.write("wibisonopanji4@gmail.com ")
    st.link_button("Dimas Wibisono", "https://www.linkedin.com/in/dimas-wibisono-53972020a/?skipRedirect=true")
    st.link_button("TensaiDimsky","https://github.com/TensaiDimsky")  
st.divider()
# -------------------------------------------------------------------------------------------------------------------------
st.title("🎓 Education")
# bootcamp
with st.expander("📊 Full Stack Data Analyst & Data Science Bootcamp", expanded=True):
    st.write("**Dibimbing.id | Jakarta**")
    st.write("*Completed: April, 2026*")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Core Skills:**")
        st.markdown("- SQL (PostgreSQL, MySQL)")
        st.markdown("- Python (Pandas, NumPy, Scikit-learn)")
        st.markdown("- Tableau, Power BI, Google Data Studio")
    
    with col2:
        st.markdown("**Machine Learning:**")
        st.markdown("- Regression (Linear, Logistic)")
        st.markdown("- Classification (Random Forest, SVM)")
        st.markdown("- Clustering (K-Means, RFM)")
    st.markdown("**Projects:** End-to-end data science projects from data cleaning to deployment")
    st.markdown("**Soft skills:** Data storytelling, problem-solving, business communication")
        
#-----------------------------------------------------------------------------------------------------------------

# University Section
with st.expander("📘 S.Si in Physics – Material Science", expanded=True):
    st.write("**Universitas Diponegoro (UNDIP) | Semarang**")
    st.write("*Graduated: February, 2025*")
    
    st.markdown("**Undergraduate Thesis (Skripsi):**")
    st.write("Preparation of S/AC/MWCNT-Based Electrodes with Mass Variation on Activated Carbon")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Relevant Coursework:**")
        st.markdown("- Material Characterization Techniques")
        st.markdown("- Computational Physics & Data Analysis")
    with col2:
        st.markdown("- Solid State Physics")
        st.markdown("- Statistical Data Modeling")


st.divider()
#--------------------------------------------------------------------------------------------------------------------------
st.title('Heres My Portofolio as Data Analyst & Data Science')

tab1, tab2, tab3, tab4 = st.tabs(["📊 Project 1", "📈 Project 2", "📋 Project 3", "📄 Project 4"])

with tab1:
    st.subheader("**📊 PROJECT 1:SALES PERFORMANCE ANALYSIS**")
    st.markdown("Sales Analysis for Fashion Brands in Australia")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Brief Description:**
        - Sales analysis for a new fashion brand in Australia
        - Identifying the factors behind the decline in sales in October 2021
        - Providing data-driven marketing strategy recommendations
        
        **Tech Stack:** Python, Pandas, Power BI, Looker Studio, Google Colab
        """)
        st.markdown("""
    ### 🔑 Key Results
    - Identify the 3 main products accounting for over 30% of sales
    - Identify sales patterns, with a peak on Sundays (520 orders) and a low on Mondays (240 orders)
    - Map product preferences by region to inform regional strategy
    
    ### 💡 Business Recomendation
    - Marketing strategy recommendations ready for implementation within 4 weeks
    - Target of a 25% increase in Monday sales
    - Projected 15% increase in customer acquisition from 2 potential regions
    """)
    with col2:
        st.markdown("**📁 Link Resources:**")
        st.link_button("📓 Work Result", "https://drive.google.com/drive/folders/1kXqYeLLWi2mjxKhgdQStdqJoTZ8MwXgf?usp=sharing")

with tab2:
    st.subheader("🚚 PROJECT 2: Predicting Delivery Times Using Machine Learning")
    st.markdown("End-to-End Machine Learning Project for Logistics Optimisation")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Brief Description:**
        - Building a machine learning model to **predict food delivery times**
        - Identifying critical factors influencing delivery delays
        - Dataset: 1,000 rows of field data with 9 features (distance, weather, traffic, vehicle type, etc.)
        - Implementation of 4 ML algorithms: Ridge, Lasso, Random Forest, XGBoost
        - **Best Model:** Random Forest with R² = 0.78 and MAPE = 12.9%
        
        **Tech Stack:** Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, XGBoost, Streamlit
        """)

          # Key Findings
        st.markdown("**🔑 Key Findings:**")
        st.markdown("""
        - **Distance travelled** is the most significant factor (35% influence)
        - **Kitchen preparation time** accounts for 25% of the total delivery time
        - **Rainy/snowy weather** can slow down deliveries by up to 80%
        - **Heavy traffic** increases delivery time by 22% compared to light traffic
        
        ### 💡 Business Recomendation
        - Prioritise the accuracy of distance data - Ensure that the mapping and courier route systems are accurate
        - Optimise kitchen preparation time - Aim for an average preparation time of less than 15 minutes
        - Allow extra time during peak periods Add 10-15 minutes to the usual estimated time
        """)
    
    with col2:
        st.markdown("**📁 Link Resources:**")
        st.link_button("📓 Work Result", "https://drive.google.com/drive/folders/1j2kNJRfVmrCo_HGsSrb_EkStG1bkPv4b?usp=sharing")


    with tab3:
        st.subheader("📞 PROJECT 3: Customer Churn Analysis & Segmentation")
        st.markdown("Churn Analysis & Customer Segmentation for the Telecommunications Industry")

        col1, col2 = st.columns([2, 1])
    
        with col1:
            st.markdown("""
        **Brief Description:**
        - Analysis of the churn rate of **26.5%** and identification of the factors causing churn
        - Implementation of **K-Means Clustering** for customer segmentation based on behaviour
        - Dataset: 7,043 customers with 38 features (demographics, services, payments, tenure)
        - Dividing customers into **4 distinct segments** with different retention strategies
        - Providing business recommendations for each customer segment
        
        **Tech Stack:** Python, Scikit-learn (K-Means), Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit
        """)

        # Key Findings
        st.markdown("**🔑 Key Findings:**")
        st.markdown("""
        - **Month-to-month contracts** have the highest churn risk (~50% vs 2.7% for 2-year contracts)
        - **Electronic cheques** as a payment method have the highest churn rate
        - **Fibre optic** customers have a churn rate of ~40% (the highest among internet types)
        - **No Offer** customers: 37.5% churn rate – critical to provide an offer
        - **No Online Security** significantly increases the risk of churn
                    
        ### 💡 Business Recomendation
        - Switching to direct debit is a top priority
        - All customers must be offered a special deal
        - Loyalty rewards for customers who have been subscribed for a certain period of time can be used to prevent churn    
        """)
    
        with col2:
            st.markdown("**📁 Link Resources:**")
            st.link_button("📓 Work Result", "https://drive.google.com/drive/folders/1EszMbVlnQDxzvUiopEWaFvwr5UTn-lBx?usp=sharing")    


    with tab4 :
        st.subheader("🫁 PROJECT 4: Lung Cancer Prediction Using Machine Learning")    
        st.markdown("Early Detection of Lung Cancer Using Machine Learning")

        col1, col2 = st.columns([2, 1])
    
        with col1:
            st.markdown("""
        **Brief Description:**
        - Building a machine learning model for **early detection of lung cancer**
        - Identifying the dominant risk factors influencing cancer diagnosis
        - Dataset: 1,500 patients with 9 features (age, gender, BMI, smoking, genetic risk, physical activity, alcohol consumption, history of cancer)
        - Implementation of 4 ML algorithms: Ridge, Lasso, Random Forest, XGBoost
        - **Best Model:** XGBoost with 91% accuracy and an AUC-ROC of 0.94
        
        **Tech Stack:** Python, Scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn, Streamlit
        """)
        
        # Key Findings
            st.markdown("**🔑 Key Findings:**")
            st.markdown("""
        - **Lifestyle and genetic factors** are the most dominant predictors
        - **Smoking & Genetic Risk** are the top two features in terms of importance
        - Dataset: 943 patients (62.9%) without cancer, 557 patients (37.1%) with cancer
        - **XGBoost** outperforms other models with 91% accuracy
        - The model is able to detect 88% of cancer cases (Recall)
        
        ### 💡Recomendation
        - Raise public awareness and provide education on cancer risk factors
        - Development of a sustainable monitoring system by developing a web-based or mobile monitoring system that utilises this model, so that the public can carry out regular self-checks.
        """)
    
        with col2:
            st.markdown("**📁 Link Resources:**")
            st.link_button("📓 Work Result", "https://drive.google.com/drive/folders/1dQnSBQF7yzciSGUC2EHp3r5Kr2Z_6t2L?usp=sharing")
 

