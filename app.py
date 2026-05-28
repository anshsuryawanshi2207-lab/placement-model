import streamlit as st
import numpy as np
import joblib


st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎓",
    layout="centered"
)


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

/* TITLE */
h1 {
    color: #00FFD1 !important;
    text-align: center;
    font-size: 45px !important;
    font-weight: bold;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: white;
    font-size: 20px;
    margin-bottom: 20px;
}

/* INPUT LABELS */
label {
    color: white !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

/* NUMBER INPUT LABEL */
div.stNumberInput label {
    color: white !important;
    font-weight: bold !important;
}

/* SELECTBOX LABEL */
div.stSelectbox label {
    color: white !important;
    font-weight: bold !important;
}

/* SLIDER LABEL FIX */
div[data-baseweb="slider"] label {
    color: white !important;
    font-size: 16px !important;
    font-weight: bold !important;
}

/* BUTTON */
.stButton > button {
    background-color: #00FFD1;
    color: black;
    font-size: 20px;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #00c9a7;
    color: white;
}

/* SUCCESS BOX */
.stSuccess {
    border-radius: 12px;
}

/* ERROR BOX */
.stError {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


model = joblib.load("placement_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🎓 AI Student Placement Predictor")

st.markdown(
    "<div class='subtitle'>Predict Student Placement using Machine Learning 🚀</div>",
    unsafe_allow_html=True
)

st.write("")


col1, col2 = st.columns(2)

with col1:

    st.subheader("📘 Academic Details")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=30,
        value=20
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    degree = st.selectbox(
        "Degree",
        ["B.Tech", "BCA", "M.Tech", "MCA"]
    )

    branch = st.selectbox(
        "Branch",
        ["CSE", "AIML", "ECE", "IT", "ME"]
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0
    )

    internships = st.number_input(
        "Internships",
        min_value=0,
        max_value=10,
        value=1
    )

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=20,
        value=2
    )

with col2:

    st.subheader("💻 Skills Details")

    coding_skills = st.slider(
        "Coding Skills",
        min_value=0,
        max_value=10,
        value=5
    )

    communication_skills = st.slider(
        "Communication Skills",
        min_value=0,
        max_value=10,
        value=5
    )

    aptitude = st.number_input(
        "Aptitude Test Score",
        min_value=0,
        max_value=100,
        value=50
    )

    soft_skills = st.slider(
        "Soft Skills Rating",
        min_value=0,
        max_value=10,
        value=5
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=1
    )

    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=10,
        value=0
    )


gender_map = {
    "Female": 0,
    "Male": 1
}

degree_map = {
    "B.Tech": 0,
    "BCA": 1,
    "M.Tech": 2,
    "MCA": 3
}

branch_map = {
    "CSE": 0,
    "AIML": 1,
    "ECE": 2,
    "IT": 3,
    "ME": 4
}

gender = gender_map[gender]
degree = degree_map[degree]
branch = branch_map[branch]


st.write("")
st.write("")

if st.button("🚀 Predict Placement"):

    features = np.array([[
        age,
        gender,
        degree,
        branch,
        cgpa,
        internships,
        projects,
        coding_skills,
        communication_skills,
        aptitude,
        soft_skills,
        certifications,
        backlogs
    ]])

   
    features_scaled = scaler.transform(features)

   
    prediction = model.predict(features)

  
    probability = model.predict_proba(features_scaled)[0][1]

    st.write("")

    if prediction[0] == 1:

        st.success("🎉 Student Will Be Placed")

        st.progress(int(probability * 100))

        st.markdown(
            f"""
            <h2 style='color:#00FFAA; text-align:center;'>
            Placement Probability: {probability*100:.2f}%
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    else:

        st.error("❌ Student Will NOT Be Placed")

        st.progress(int(probability * 100))

        st.markdown(
            f"""
            <h2 style='color:red; text-align:center;'>
            Placement Probability: {probability*100:.2f}%
            </h2>
            """,
            unsafe_allow_html=True
        )


st.write("")
st.write("")

st.markdown(
    """
    <center>
        <h4 style='color:white;'>
        Made By Ansh Suryawanshi using Streamlit & Machine Learning
        </h4>
    </center>
    """,
    unsafe_allow_html=True
)