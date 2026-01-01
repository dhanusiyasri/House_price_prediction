# 🏠 House Price Prediction using Random Forest Regressor 🌲

This project is an **end-to-end Machine Learning web application** that predicts **house prices** based on key property features.  
It uses a **Random Forest Regressor**, an ensemble learning algorithm, and is deployed as an **interactive Streamlit web app**.

---

## 📌 Problem Statement

Estimating house prices manually is difficult due to the influence of multiple factors such as house size, number of rooms, and construction year.  
This project aims to build a **machine learning–based solution** that predicts house prices accurately using historical housing data.

---

## 🚀 Features
- 🌲 House price prediction using **Random Forest Regressor**
- 🧠 Learns non-linear relationships in housing data
- 🖥 Interactive **Streamlit web interface**
- 🎛 Sidebar inputs for real-time user interaction
- 💰 Instant predicted house price output

---

## 🧠 Machine Learning Model
### Random Forest Regressor 🌲

- An **ensemble learning algorithm**
- Uses **multiple decision trees**
- Final prediction is the **average of all trees**
- Reduces overfitting and improves accuracy
- Works very well with tabular, real-world datasets

---

## 📊 Dataset
- **Source:** Kaggle – *House Prices: Advanced Regression Techniques*
- **File Used:** `train.csv`
- **Total Records:** 1460 houses

### Selected Features
- `GrLivArea` – Above ground living area (sq ft)
- `BedroomAbvGr` – Number of bedrooms
- `FullBath` – Number of full bathrooms
- `YearBuilt` – Year the house was built
- `SalePrice` – Target variable (house price)

Rows with missing values are removed during preprocessing.

---

## ✂️ Train–Test Split
- **Training Data:** 80% → 1168 houses
- **Testing Data:** 20% → 292 houses

The test set is kept unseen during training to evaluate model performance fairly.

---

## 🗂 Project Structure

house-price-prediction/
```
│
├── app.py # Streamlit web application
├── train.csv # Housing dataset
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```
---

## ⚙️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Random Forest Regressor
- Streamlit
- Matplotlib

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit App

```bash
 streamlit run app.py
```

### 3️⃣ Open in Browser
```bash
 http://localhost:8501
 ```

 ---


## 🖥 How the Application Works

- Loads the housing dataset (train.csv)

- Selects important features and removes missing values

- Trains a Random Forest Regressor

- Accepts house details from the user via sidebar inputs

- Predicts and displays the estimated house price instantly

---

## 🎯 Sample Output

- User enters house details (area, bedrooms, bathrooms, year built)

- The model predicts the estimated house price

- Result is displayed clearly in the web interface

---

## 👩‍💻 Author

Dhanusiya Sri M
Computer Science Engineering Student
Aspiring Machine Learning & Data Analytics Enthusiast

