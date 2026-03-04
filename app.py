import streamlit as st
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Exam Performance Predictor", page_icon="📚", layout="centered")

st.title("📚 Student Exam Performance Predictor")
st.markdown("### Predict your **Math Score** based on your profile")

st.divider()

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", options=["male", "female"])

        race_ethnicity = st.selectbox(
            "Race / Ethnicity",
            options=["group A", "group B", "group C", "group D", "group E"],
        )

        parental_level_of_education = st.selectbox(
            "Parental Level of Education",
            options=[
                "associate's degree",
                "bachelor's degree",
                "high school",
                "master's degree",
                "some college",
                "some high school",
            ],
        )

    with col2:
        lunch = st.selectbox("Lunch Type", options=["free/reduced", "standard"])

        test_preparation_course = st.selectbox(
            "Test Preparation Course", options=["none", "completed"]
        )

        reading_score = st.number_input(
            "Reading Score (out of 100)", min_value=0, max_value=100, value=50
        )

        writing_score = st.number_input(
            "Writing Score (out of 100)", min_value=0, max_value=100, value=50
        )

    submitted = st.form_submit_button("🎯 Predict your Math Score")

if submitted:
    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=float(reading_score),
        writing_score=float(writing_score),
    )

    pred_df = data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    st.success(f"🎓 Predicted Math Score: **{results[0]:.2f}**")