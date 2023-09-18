import streamlit as st
import requests
import json

st.title("Titanic Survival Prediction")

# Input form
st.sidebar.header("Enter Passenger Information")
pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
sex = st.sidebar.radio("Gender", ["male", "female"])
age = st.sidebar.slider("Age", 1, 100, 25)
sibsp = st.sidebar.slider("Number of Siblings/Spouses Aboard", 0, 8, 0)
parch = st.sidebar.slider("Number of Parents/Children Aboard", 0, 6, 0)

# Predict button
if st.sidebar.button("Predict"):
    input_data = {
        "Pclass": pclass,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Sex_male": 1 if sex=='male' else 0,
    }

    # Send a POST request to your Flask API for prediction
    response = requests.post("http://localhost:5000/predict", json=input_data)

    # Display the prediction result
    if response.status_code == 200:
        result = response.json()["predictions"][0]
        if result == 1:
            st.success("Survived")
        else:
            st.error("Did Not Survive")
    else:
        st.error("Failed to make a prediction. Check your input data.")

