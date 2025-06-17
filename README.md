# 🩺 PCOS Risk Prediction Web App

A Machine Learning-powered web application to predict the risk of Polycystic Ovary Syndrome (PCOS) based on user symptoms and health data.

## 📌 Project Overview

Polycystic Ovary Syndrome (PCOS) is a hormonal disorder affecting many women worldwide. Early detection and awareness can help manage symptoms effectively. This project uses machine learning to predict the likelihood of PCOS based on various health and lifestyle inputs, presented through a user-friendly Flask web application.

## 🚀 Features

- 🧠 Machine Learning model with ~89% accuracy.
- 📊 Auto-calculates BMI, Cycle Score, Waist-to-Weight ratio, etc.
- 🖥️ Three simple pages: 
  - **Information Page**
  - **User Input Page**
  - **Prediction Result Page**
- 🌸 Soft pastel UI theme for readability and comfort.
- 🔒 Privacy-focused – no user data is stored permanently.

## 📂 Project Structure


pcos-predictor/
├── static/
│ └── style.css # Custom CSS for the website
├── templates/
│ ├── info.html # Info page (definition, causes, symptoms, risks)
│ ├── form.html # User input form
│ └── result.html # Prediction results
├── model/
│ └── rf_model.pkl # Trained ML model file
├── app1.py # Main Flask app
├── requirements.txt # Python dependencies
└── README.md # Project documentation

🛠️ Tech Stack
Frontend: HTML, CSS (Pastel-themed)

Backend: Python, Flask

ML Libraries: scikit-learn, pandas, numpy

Data Source: Public PCOS dataset (Kaggle)

📈 ML Model Info
Algorithm Used: [Mention the best-performing algorithm, e.g., Random Forest, XGBoost, etc.]

Balanced Data: Used SMOTE for oversampling

Performance Metrics:

Accuracy: ~89%

Precision, Recall, F1 Score: Also balanced