
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/marks_model.pkl")

st.title("Student Marks Prediction System")

st.write("""
Predict final board exam percentage using
Machine Learning Regression.
""")

st.divider()

marks = st.slider(
    "PreBoard Marks",
    0,
    100,
    50
)

attendance = st.slider(
    "Attendance Percentage",
    0,
    100,
    75
)

study_hours = st.slider(
    "Study Hours Per Day",
    0,
    10,
    3
)

assignments = st.selectbox(
    "Assignments Submitted",
    ["Yes", "No"]
)

sleep_hours = st.slider(
    "Sleep Hours",
    0,
    12,
    6
)

assignments_value = 1 if assignments == "Yes" else 0

if st.button("Predict Percentage"):

    input_data = pd.DataFrame([[
        marks,
        attendance,
        study_hours,
        assignments_value,
        sleep_hours
    ]], columns=[
        'PreBoardMarks',
        'Attendance',
        'StudyHours',
        'Assignments',
        'SleepHours'
    ])

    prediction = model.predict(input_data)

    predicted_marks = prediction[0]

    st.divider()

    st.success(
        f"Predicted Final Percentage: {predicted_marks:.2f}%"
    )

    if predicted_marks >= 85:
        st.balloons()
        st.success("Excellent Performance Expected!")

    elif predicted_marks >= 70:
        st.info(" Good Academic Performance")

    elif predicted_marks >= 50:
        st.warning("Average Performance")

    else:
        st.error("Student Needs Serious Improvement")

    st.subheader("Suggestions")

    if attendance < 75:
        st.write("Improve attendance.")

    if study_hours < 3:
        st.write("Increase study hours.")

    if assignments_value == 0:
        st.write("Submit assignments regularly.")

    if sleep_hours < 6:
        st.write("Improve sleep schedule.")

