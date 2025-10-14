Fake Job Post Detection using ML and NLP

A Machine Learning-based web application that detects fake job postings using NLP and classification algorithms.
The system analyzes job descriptions and predicts whether a job post is Authentic or Fake, helping users avoid scams.

Project Overview

With the increasing number of online job scams, it’s crucial to automatically identify fake job listings.
This project uses Natural Language Processing (NLP) and Machine Learning models to analyze textual job descriptions and determine their authenticity.

The trained model is integrated with a Flask web application, providing a user-friendly interface where users can enter job descriptions and get instant predictions.

Features

 Analyze Job Descriptions – Detect if a post is fake or authentic.

 Multiple ML Models Tested – Logistic Regression, Random Forest, LightGBM, XGBoost, LinearSVC, MultinomialNB, and Ensemble models.

 Best Model: Voting Ensemble – Achieved the highest F1-score (~0.73) among all models.

 Comprehensive Evaluation – Includes confusion matrices, ROC curves, PR curves, and feature importance plots.

 Flask Web App – Simple and elegant interface for testing job descriptions.

 Models & Performance
Model	F1-Score (CV)
Voting Ensemble	0.73
LightGBM	0.72
Random Forest	0.71
Stacking Ensemble	0.71
XGBoost	0.69
LinearSVC	0.62
Logistic Regression	0.58
MultinomialNB	0.47

📈 Voting Ensemble achieved the best results in terms of F1-score.

 Project Structure
Fake_Job_Post_Detection/
│
├── app/
│   ├── app.py                  # Flask backend
│   ├── templates/
│   │   └── index.html          # Frontend UI
│   ├── static/
│       └── styles.css          # Styling
│
├── models/
│   ├── VotingEnsemble_final.joblib
│   ├── tfidf_vectorizer.joblib
│   └── other_model_files...
│
├── reports/
│   ├── model_comp_f1_cv.png
│   ├── cm_*.png, pr_*.png, roc_*.png, feat_imp_*.png
│   └── cv_summary.csv, test_summary.csv
│
├── data/
│   └── fake_job_postings.csv   # Original dataset
│
├── requirements.txt
├── README.md
└── .gitignore

 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Nithyanandhana/Fake_Job_Post_Detection.git
cd Fake_Job_Post_Detection

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate       # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
cd app
python app.py


Your app will start on → http://127.0.0.1:5000/

 Testing

Enter any job description in the input box to test whether it is Fake or Authentic.

 Results Summary

Best Performing Model: Voting Ensemble

Evaluation Metric: F1-Score (to balance precision & recall)

Vectorization Technique: TF-IDF

Language: Python

Framework: Flask
