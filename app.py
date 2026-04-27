
    import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🚦 Traffic Signal Timing Prediction")

st.write("Enter traffic conditions")

# Inputs
traffic = st.slider("Traffic Volume", 0, 500, 100)
speed = st.slider("Average Speed (km/h)", 0, 60, 30)
hour = st.slider("Hour", 0, 23, 12)

# Prediction
if st.button("Predict"):
    input_data = np.array([[traffic, speed, hour]])
    prediction = model.predict(input_data)

    st.success(f"Green Signal Time: {prediction[0]:.2f} sec")
    