from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model and vectorizer
model = joblib.load('../train/sms_spam_classifier.pkl')
vectorizer = joblib.load('../train/tfidf_vectorizer.pkl')

# Create a Flask application
app = Flask(__name__)

@app.route('/predict_sms', methods=['POST'])
def predict_sms():
    # Get the SMS from the request body
    data = request.json
    sms = data.get('sms')

    if not sms:
        return jsonify({"error": "No SMS provided"}), 400

    # Preprocess the SMS
    sms = sms.lower().replace('[^\w\s]', '')
    sms_features = vectorizer.transform([sms])
    
    # Predict
    prediction = model.predict(sms_features)[0]
    
    # Convert prediction to human-readable form
    result = 'spam' if prediction == 'spam' else 'ham'
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
