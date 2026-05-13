import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("knn_model.pkl", "rb"))

st.title("KNN Regression App")

# Inputs
age = st.number_input("Age", min_value=18, max_value=100)

income = st.number_input("Income")

loan_amount = st.number_input("Loan Amount")

credit_score = st.number_input("Credit Score")

city = st.selectbox(
    "City",
    ["Bangalore", "Chennai", "Hyderabad", "Mumbai"]
)

employment_type = st.selectbox(
    "Employment Type",
    ["Salaried", "Self-Employed", "Unemployed"]
)

# Predict
if st.button("Predict"):

    input_data = pd.DataFrame({

        "age": [age],
        "income": [income],
        "loan_amount": [loan_amount],
        "credit_score": [credit_score],

        "city_Bangalore": [1 if city == "Bangalore" else 0],
        "city_Chennai": [1 if city == "Chennai" else 0],
        "city_Hyderabad": [1 if city == "Hyderabad" else 0],
        "city_Mumbai": [1 if city == "Mumbai" else 0],

        "employment_type_Salaried": [
            1 if employment_type == "Salaried" else 0
        ],

        "employment_type_Self-Employed": [
            1 if employment_type == "Self-Employed" else 0
        ],

        "employment_type_Unemployed": [
            1 if employment_type == "Unemployed" else 0
        ]

    })

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")