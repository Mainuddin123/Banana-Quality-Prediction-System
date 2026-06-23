import streamlit as st
import pandas as pd
import joblib

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Banana Quality Prediction",
    page_icon="🍌",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

/* Text */
h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

/* Number Inputs */
.stNumberInput input{
    background-color:#1f2937 !important;
    color:white !important;
}

/* Dropdowns */
.stSelectbox div[data-baseweb="select"]{
    background:white !important;
    border-radius:8px;
}

.stSelectbox div[data-baseweb="select"] *{
    color:black !important;
    font-weight:600 !important;
}

/* Button */
.stButton > button{
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    ) !important;

    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;

    border:none !important;
    border-radius:12px !important;

    width:100%;
    height:60px;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:#1e293b;
    border:1px solid #334155;
    border-radius:15px;
    padding:15px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load("banana_quality_knn.pkl")

# =====================================
# HEADER
# =====================================

st.markdown("""
<div style="
background:linear-gradient(
90deg,
#f59e0b,
#f97316
);
padding:25px;
border-radius:20px;
text-align:center;
">

<h1 style="color:white;">
🍌 Banana Quality Prediction System
</h1>

<h3 style="color:white;">
Machine Learning Regression Application
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# PROJECT DESCRIPTION
# =====================================

st.info("""
This intelligent system predicts banana quality based on physical,
chemical, and environmental attributes.

It can support farmers, distributors, retailers, and food quality
analysts in making data-driven quality assessment decisions.
""")

# =====================================
# KPI CARDS
# =====================================

c1, c2, c3 = st.columns(3)

c1.metric("Industry", "Agriculture")
c2.metric("Use Case", "Quality Analysis")
c3.metric("Prediction", "Quality Score")

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 Project Information")

st.sidebar.info("""
Project:
Banana Quality Prediction

Domain:
Agriculture Analytics

Goal:
Predict Banana Quality Score

Application:
Quality Assessment

Users:
Farmers
Distributors
Retailers
Food Quality Analysts
""")

# =====================================
# INPUT SECTION
# =====================================

st.subheader("📝 Enter Banana Details")

col1, col2 = st.columns(2)

with col1:

    variety = st.selectbox(
        "Variety",
        ["Cavendish", "Plantain", "Red Dacca", "Burro", "Manzano"]
    )

    region = st.selectbox(
        "Region",
        ["Ecuador", "Colombia", "Guatemala"]
    )

    ripeness_category = st.selectbox(
        "Ripeness Category",
        ["Unripe", "Turning", "Ripe", "Overripe"]
    )

    ripeness_index = st.number_input(
        "Ripeness Index",
        value=4.0
    )

    sugar_content_brix = st.number_input(
        "Sugar Content Brix",
        value=18.0
    )

    firmness_kgf = st.number_input(
        "Firmness KGF",
        value=2.5
    )

with col2:

    length_cm = st.number_input(
        "Length (cm)",
        value=20.0
    )

    weight_g = st.number_input(
        "Weight (g)",
        value=160.0
    )

    tree_age_years = st.number_input(
        "Tree Age (Years)",
        value=10.0
    )

    altitude_m = st.number_input(
        "Altitude (m)",
        value=700.0
    )

    rainfall_mm = st.number_input(
        "Rainfall (mm)",
        value=2000.0
    )

    soil_nitrogen_ppm = st.number_input(
        "Soil Nitrogen PPM",
        value=100.0
    )

# =====================================
# PREDICTION
# =====================================

if st.button("🚀 Predict Quality Score"):

    input_data = pd.DataFrame({
        "variety":[variety],
        "region":[region],
        "ripeness_index":[ripeness_index],
        "ripeness_category":[ripeness_category],
        "sugar_content_brix":[sugar_content_brix],
        "firmness_kgf":[firmness_kgf],
        "length_cm":[length_cm],
        "weight_g":[weight_g],
        "tree_age_years":[tree_age_years],
        "altitude_m":[altitude_m],
        "rainfall_mm":[rainfall_mm],
        "soil_nitrogen_ppm":[soil_nitrogen_ppm]
    })

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    st.subheader("🎯 Prediction Results")

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Quality Score",
        f"{prediction:.2f}"
    )

    if prediction >= 3:

        category = "Premium"

        r2.metric(
            "Category",
            category
        )

        st.success(
            "🏆 Premium Quality Banana"
        )

    elif prediction >= 2:

        category = "Standard"

        r2.metric(
            "Category",
            category
        )

        st.warning(
            "⭐ Standard Quality Banana"
        )

    else:

        category = "Processing"

        r2.metric(
            "Category",
            category
        )

        st.error(
            "⚠️ Processing Grade Banana"
        )

    r3.metric(
        "Industry",
        "Agriculture"
    )

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown("""
<div style="
background:linear-gradient(
90deg,
#1e293b,
#0f172a
);
padding:25px;
border-radius:20px;
text-align:center;
">

<h2 style="color:white;">
Khaja Mainuddin
</h2>

<h4 style="color:#38bdf8;">
Artificial Intelligence and Data Science Graduate
</h4>

<p style="color:white;">
Machine Learning • Data Science • Python • Streamlit
</p>

<p style="color:#94a3b8;">
End-to-End Machine Learning Project
</p>

</div>
""", unsafe_allow_html=True)
