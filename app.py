# X order ->
# 'Years_At_Company','Montly_Salary','Overtime',
# 'Promotions','Employee_Satisfaction_Score'

import streamlit as st
import joblib
import numpy as np

# Load saved scaler and model
scaler = joblib.load("scaler.pkl")
model = joblib.load("decision_tree_model.pkl")

st.title("Employee Performance Prediction")

st.divider()

st.write(
    "Enter employee details below and click **Predict** "
    "to estimate performance."
)

st.divider()

# Input fields
years = st.number_input(
    "Years at Company", min_value=0, max_value=15, value=2
)

salary = st.number_input(
    "Monthly Salary", min_value=1000, max_value=10000, value=5000
)

overtime = st.number_input(
    "Overtime Hours", min_value=0, max_value=100, value=0
)

promotion = st.number_input(
    "Number of Promotions", min_value=0, max_value=10, value=0
)

employee_satisfaction = st.number_input(
    "Employee Satisfaction Score",
    min_value=0.0, max_value=5.0, value=2.0
)

st.divider()

# Predict button
prediction_button = st.button("Predict Performance")

st.divider()

if prediction_button:
    # Convert input to numpy array (2D)
    X = np.array([[years, salary, overtime, promotion, employee_satisfaction]])

    # Scale input
    X_scaled = scaler.transform(X)

    # Prediction
    prediction = model.predict(X_scaled)[0]

    st.balloons()
    st.success(f"Predicted Employee Performance Score: {prediction}")

else:
    st.info("Click the **Predict Performance** button to see the result.")
