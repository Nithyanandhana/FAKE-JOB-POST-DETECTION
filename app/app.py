from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# ✅ Use absolute paths
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "VotingEnsemble_final.joblib")
VEC_PATH = os.path.join(BASE_DIR, "..", "models", "tfidf_vectorizer.joblib")

print("📂 Loading model and vectorizer...")
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VEC_PATH)
    print("✅ Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model/vectorizer: {e}")
    model = None
    vectorizer = None

@app.route('/')
def home():
    print("🏠 Home route accessed")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return render_template('index.html', result="❌ Model not loaded properly.")
    
    print("🔍 Predict route called")
    text = request.form['text']
    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    result = "🛑 Fake Job Post" if prediction == 1 else "✅ Authentic Job Post"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    print("🚀 Starting Flask server on http://127.0.0.1:5000/")
    app.run(debug=True)
