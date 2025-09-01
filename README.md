# FAKE-JOB-POST-DETECTION
A machine learning project to detect fake job postings using NLP, EDA, and classification models.
🚀 Fake Job Post Detection
📌 Project Overview

Online recruitment platforms are flooded with both genuine and fraudulent job postings. Fake jobs can lead to financial scams and misuse of personal data.
This project applies Machine Learning (ML) techniques to detect fake job postings based on job descriptions and related features.

🎯 Objectives

Build a classification model to detect fake job posts.

Perform EDA (Exploratory Data Analysis) to identify patterns in fraudulent jobs.

Apply text cleaning, vectorization (TF-IDF), and feature engineering.

Train and evaluate multiple ML models:

Logistic Regression

Naive Bayes

Decision Tree

Random Forest

Support Vector Machine (SVM)

XGBoost

Compare model performance and select the best fit model.

Save the final model and vectorizer for deployment-ready predictions.

📊 Dataset

Dataset size: 6,841 job postings × 18 features

Target column: fraudulent (0 = real, 1 = fake)

Features:

Text fields (title, company_profile, description, requirements, benefits)

Numeric fields (telecommuting, has_company_logo, has_questions, etc.)

⚙️ Steps Performed

Data Cleaning – removed missing labels, cleaned text, combined relevant fields.

EDA – missingness analysis, correlation heatmap, target distribution.

Feature Engineering – TF-IDF vectorization with unigrams & bigrams.

Model Training – tested 6 ML algorithms.

Cross-Validation – stratified 5-fold validation.

Evaluation – accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix.

Hyperparameter Tuning – light tuning with GridSearchCV.

Final Model – Tuned XGBoost achieved the best performance.

📈 Results

Best Model: Tuned XGBoost

Performance: Achieved the highest F1-score and ROC-AUC compared to other models.

Example Predictions:

"Work from home, $5000/week, send bank details" → FAKE

"Infosys hiring Software Engineer via official portal" → REAL

🛠️ Tech Stack

Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost

Visualization: Confusion Matrix, ROC Curves, Precision-Recall Curves
