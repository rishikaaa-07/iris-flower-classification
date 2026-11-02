
import streamlit as st
import pandas as pd
import pickle

# Load trained model and scaler
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("iris_scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered"
)

# Application heading
st.title("🌸 Iris Flower Classification")
st.subheader("Machine Learning Prediction System")

st.write(
    "Enter the flower measurements below "
    "to predict its species."
)

st.divider()

# Input fields
st.header("Enter Flower Measurements")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.1,
        max_value=10.0,
        value=5.1
    )

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.1,
        max_value=10.0,
        value=1.4
    )

with col2:
    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.1,
        max_value=10.0,
        value=3.5
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.1,
        max_value=10.0,
        value=0.2
    )

# Prediction button
if st.button("🔍 Predict Flower Species"):

    input_data = pd.DataFrame(
        [[sepal_length, sepal_width,
          petal_length, petal_width]],
        columns=[
            'sepal_length_cm',
            'sepal_width_cm',
            'petal_length_cm',
            'petal_width_cm'
        ]
    )

    # Apply scaling only for scaled models
    if st.session_state.get("model_scaled", True):
        input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    st.divider()

    st.success(
        f"🌸 Predicted Flower Species: {prediction[0]}"
    )

    st.balloons()

st.divider()

st.caption(
    "Developed using Python, Streamlit and Machine Learning"
)
