import streamlit as st
import requests

st.title("PLM Predictive Maintenance Dashboard")

st.sidebar.header("Sensor Data Input")
temperature = st.sidebar.slider("Temperature", 70, 100, 85)
vibration = st.sidebar.slider("Vibration", 2.0, 7.0, 4.5)
cycle = st.sidebar.slider("Cycle", 100, 500, 500)

if st.button("Predict Maintenance"):
    data = {
        "temperature": temperature,
        "vibration": vibration,
        "cycle": cycle
    }
    response = requests.post("http://localhost:8000/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        st.write("Prediction:", result["prediction"])
        st.write("Context:", result["context"])
    else:
        st.error("Error in prediction")