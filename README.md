# 🏡 House Price Prediction using Machine Learning

## 🔍 Project Overview

An end-to-end machine learning project that predicts house prices based on various property features such as area, bedrooms, bathrooms, stories, parking availability, furnishing status, and other amenities using the **Linear Regression** algorithm.

The project demonstrates a complete Machine Learning workflow, including Data preprocessing & Feature Engineering, Exploratory Data Analysis (EDA), model training, evaluation, and web interface to predict pricing using various features as input.

---

## 🚀 Features

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Linear Regression Model
- Model Evaluation
- Streamlit Web Application
- House Price Prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Exploratory Data Analysis

The project includes:

- Histogram of House Prices
- Correlation Heatmap
- Scatter Plot (Area vs Price)
- Boxplot
- Pairplot
- Feature Correlation Chart

---

## 🤖 Machine Learning Model

Algorithm Used:

- Linear Regression

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

---

## 📈 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Example Results:

| Metric | Value |
|---------|-------|
| MAE | ₹9.88 Lakhs |
| RMSE | ₹13.56 Lakhs |
| R² Score | 0.6364 |

---

## 📁 Project Structure

```text
House_Price_Prediction/
│
├── app.py
├── house_price_prediction.ipynb
├── Housing.csv
├── house_price_model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

### Clone the repository

```bash
git clone <your-github-repository-link>
```

### Move into the project folder

```bash
cd House_Price_Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 🖥️ Application

The Streamlit application allows users to enter:

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road Access
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

The trained model predicts the estimated selling price of the house.

---

## 📚 Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Dataset Overview
4. Data Cleaning
5. Feature Engineering
6. Exploratory Data Analysis
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Save Model
11. Deploy using Streamlit

---

## 🔮 Future Improvements

- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- Hyperparameter Tuning
- Feature Scaling
- Cloud Deployment

---

## 🧠 Key Learnings & Achievements:

- End-to-end experience—from raw data to live web app deployment.

- Hands-on exposure to feature engineering, model tuning, and deployment challenges.

- Ability to package ML pipelines for production and embed them in a user interface.

⚠️ Note: This project is for educational/demonstration purposes. Real-world implementation would require additional considerations like more extensive validation, error handling, security, and scalability.

## 👨‍💻 Author

**[Miran Wagle](https://github.com/MiranWagle)**

LinkedIn: https://www.linkedin.com/in/miran-wagle-146262323/

---
