import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Title
st.title("🏠 House Price Prediction App")

st.write("Predict house prices using Machine Learning")

# Load data
data = pd.read_csv("train.csv")

data = data[[
    "GrLivArea",
    "BedroomAbvGr",
    "FullBath",
    "YearBuilt",
    "SalePrice"
]]

data.dropna(inplace=True)

# Train model
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

model = LinearRegression()
model.fit(X, y)

# Sidebar inputs
st.sidebar.header("Enter House Details")

area = st.sidebar.number_input("Living Area (sq ft)", 500, 5000, 1500)
bedrooms = st.sidebar.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.sidebar.number_input("Bathrooms", 1, 5, 2)
year_built = st.sidebar.number_input("Year Built", 1900, 2024, 2005)

# Prediction
input_data = [[area, bedrooms, bathrooms, year_built]]
prediction = model.predict(input_data)

# Output
st.subheader("💰 Predicted House Price")
st.success(f"₹ {prediction[0]:,.0f}")

