import streamlit as st
import numpy as np
import joblib

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Placement Readiness Coach",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
           
/* Radio Question */
[data-testid="stRadio"] label p {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Radio Option Text */
[data-baseweb="radio"] div {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Make all markdown text white */
.stMarkdown p {
    color: white !important;
}

/* Radio question text */
div[data-testid="stRadio"] > label {
    color: white !important;
    font-size: 20px !important;
    font-weight: bold !important;
}


.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

h1 {
    color: #00FFD1 !important;
    text-align: center;
    font-size: 45px !important;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 20px;
    margin-bottom: 20px;
}

label {
    color: white !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

div.stNumberInput label,
div.stSelectbox label {
    color: white !important;
    font-weight: bold !important;
}

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

.stSuccess,
.stError {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #
model = joblib.load("placement_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- TITLE ---------------- #
st.title("🎓 AI Placement Readiness Coach")

st.markdown(
    """
    <div class='subtitle'>
    Predict Placement Chances & Get Personalized Improvement Tips 🚀
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- INPUT COLUMNS ---------------- #
col1, col2 = st.columns(2)

# ================= ACADEMIC DETAILS ================= #
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
        value=7.0,
        step=0.1
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

# ================= SKILLS DETAILS ================= #
with col2:

    st.subheader("💡 Skills Details")

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

# ================= CODING ASSESSMENT ================= #
st.markdown("---")
st.subheader("💻 Coding Assessment")

q1 = st.radio(
    "1. What is the output of print(2**3)?",
    ["5", "6", "8", "9"]
)

q2 = st.radio(
    "2. Which data structure follows FIFO?",
    ["Stack", "Queue", "Tree", "Graph"]
)

q3 = st.radio(
    "3. Time complexity of Binary Search?",
    ["O(n)", "O(log n)", "O(n²)", "O(1)"]
)

q4 = st.radio(
    "4. Which keyword is used to define a function in Python?",
    ["func", "define", "def", "function"]
)

q5 = st.radio(
    "5. Which sorting algorithm has average complexity O(n log n)?",
    ["Bubble Sort", "Selection Sort", "Merge Sort", "Insertion Sort"]
)

coding_score = 0

if q1 == "8":
    coding_score += 1

if q2 == "Queue":
    coding_score += 1

if q3 == "O(log n)":
    coding_score += 1

if q4 == "def":
    coding_score += 1

if q5 == "Merge Sort":
    coding_score += 1

# Convert to 0–10 scale
coding_skills = round((coding_score / 5) * 10)

st.info(f"💻 Coding Score: {coding_skills}/10")


# ================= COMMUNICATION ASSESSMENT ================= #
st.markdown("---")
st.subheader("🗣️ Communication Assessment")

answer = st.text_area(
    "Describe yourself in 100–150 words",
    placeholder="""
Example:
I am a passionate and hardworking student who enjoys solving problems
and building real-world projects. I have experience working in teams,
participating in hackathons, and continuously improving my technical skills.
"""
)

# Basic Communication Score Calculation
communication_skills = 0

if answer.strip() != "":

    word_count = len(answer.split())

    # Base Score
    communication_skills = 4

    # Word Count Evaluation
    if word_count >= 50:
        communication_skills += 2

    if word_count >= 100:
        communication_skills += 2

    # Sentence Structure
    if "." in answer:
        communication_skills += 1

    # Vocabulary Diversity
    unique_words = len(set(answer.lower().split()))

    if unique_words >= 30:
        communication_skills += 1

communication_skills = min(communication_skills, 10)

st.info(
    f"🗣️ Communication Score: {communication_skills}/10"
)

# ================= ENCODING ================= #
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

gender_encoded = gender_map[gender]
degree_encoded = degree_map[degree]
branch_encoded = branch_map[branch]

st.write("")
st.write("")

# ================= PREDICTION ================= #
if st.button("🚀 Predict Placement"):

    features = np.array([[
        age,
        gender_encoded,
        degree_encoded,
        branch_encoded,
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

    try:
        # Scale features
        features_scaled = scaler.transform(features)

        # Prediction
        prediction = model.predict(features_scaled)

        # Probability
        probability = model.predict_proba(
            features_scaled
        )[0][1]

    except:

        # Fallback if model wasn't trained on scaled data
        prediction = model.predict(features)

        probability = model.predict_proba(
            features
        )[0][1]

    st.markdown("---")

    if prediction[0] == 1:

        st.success("🎉 Student Will Be Placed!")

        st.progress(probability)

        st.markdown(
            f"""
            <h2 style='color:#00FFAA;
            text-align:center;'>

            Placement Probability:
            {probability*100:.2f}%

            </h2>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    else:

        st.error("❌ Student May NOT Be Placed")

        st.progress(probability)

        st.markdown(
            f"""
            <h2 style='color:red;
            text-align:center;'>

            Placement Probability:
            {probability*100:.2f}%

            </h2>
            """,
            unsafe_allow_html=True
        )

            # ================= PLACEMENT READINESS DASHBOARD ================= #
    st.markdown("---")
    st.subheader("📊 Placement Readiness Dashboard")

    st.write("### 💻 Coding Skills")
    st.progress(coding_skills / 10)
    st.write(f"{coding_skills}/10")

    st.write("### 🗣️ Communication Skills")
    st.progress(communication_skills / 10)
    st.write(f"{communication_skills}/10")

    st.write("### 🧠 Aptitude")
    st.progress(aptitude / 100)
    st.write(f"{aptitude}/100")

    st.write("### 🤝 Soft Skills")
    st.progress(soft_skills / 10)
    st.write(f"{soft_skills}/10")

    st.write("### 🎓 CGPA")
    st.progress(cgpa / 10)
    st.write(f"{cgpa}/10")

    # ================= WEAK AREA DETECTION ================= #
    st.markdown("---")
    st.subheader("📌 Areas to Improve")

    weak_areas = []

    if coding_skills < 7:
        weak_areas.append("Coding Skills")

    if communication_skills < 7:
        weak_areas.append("Communication Skills")

    if aptitude < 70:
        weak_areas.append("Aptitude")

    if soft_skills < 7:
        weak_areas.append("Soft Skills")

    if cgpa < 7:
        weak_areas.append("CGPA")

    if internships == 0:
        weak_areas.append("Internships")

    if projects < 2:
        weak_areas.append("Projects")

    if certifications < 2:
        weak_areas.append("Certifications")

    if backlogs > 0:
        weak_areas.append("Backlogs")

    if len(weak_areas) == 0:
        st.success("🎉 Great! You don't have any major weak areas.")
    else:
        for area in weak_areas:
            st.warning(f"⚠️ Focus on improving {area}")

    # ================= PERSONALIZED RECOMMENDATIONS ================= #
    st.markdown("---")
    st.subheader("💡 Personalized Recommendations")

    if coding_skills < 7:
        st.info(
            "💻 Solve 2–3 LeetCode problems daily and practice DSA regularly."
        )

    if communication_skills < 7:
        st.info(
            "🗣️ Practice mock interviews and improve spoken English."
        )

    if aptitude < 70:
        st.info(
            "🧠 Spend 30 minutes daily on aptitude preparation."
        )

    if internships == 0:
        st.info(
            "🏢 Try completing at least one internship."
        )

    if projects < 2:
        st.info(
            "🚀 Build 2–3 real-world projects and upload them to GitHub."
        )

    if certifications < 2:
        st.info(
            "📜 Complete certifications from Coursera, Udemy, or NPTEL."
        )

    if backlogs > 0:
        st.info(
            "📚 Clear your backlogs as early as possible."
        )

    # ================= IMPROVEMENT SIMULATOR ================= #
    st.markdown("---")
    st.subheader("🚀 Improvement Simulator")

    improved_features = features.copy()

    improved_features[0][7] = min(coding_skills + 2, 10)
    improved_features[0][8] = min(communication_skills + 2, 10)

    try:
        improved_scaled = scaler.transform(improved_features)

        improved_probability = model.predict_proba(
            improved_scaled
        )[0][1]

    except:
        improved_probability = model.predict_proba(
            improved_features
        )[0][1]

    st.success(
        f"""
        If you improve your Coding and Communication skills by 2 points,
        your placement probability may increase from
        {probability*100:.1f}% to
        {improved_probability*100:.1f}%.
        """
    )

    # ================= FINAL REPORT ================= #
    st.markdown("---")
    st.subheader("🏆 Final Placement Coach Report")

    readiness_score = (
        coding_skills +
        communication_skills +
        (aptitude / 10) +
        soft_skills +
        cgpa
    ) / 5

    st.metric(
        "🎯 Placement Readiness Score",
        f"{readiness_score:.1f}/10"
    )

    if readiness_score >= 8:
        st.success(
            "🌟 Excellent! You are highly prepared for placements."
        )

    elif readiness_score >= 6:
        st.warning(
            "👍 You are on the right track, but some improvements can boost your chances."
        )

    else:
        st.error(
            "📈 You need significant improvement before placements."
        )

       



st.markdown(
    """
    <center>
        <h4 style='color:white;'>
        Made By Ansh Suryawanshi using Streamlit & Machine Learning ❤️
        </h4>
    </center>
    """,
    unsafe_allow_html=True
) 