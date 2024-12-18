from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load('../train/sms_spam_classifier.pkl')
vectorizer = joblib.load('../train/tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/predict_sms', methods=['POST'])
def predict_sms():
    data = request.json
    sms = data.get('sms')

    if not sms:
        return jsonify({"error": "No SMS provided"}), 400

    sms = sms.lower().replace('[^\w\s]', '')
    sms_features = vectorizer.transform([sms])
    
    prediction = model.predict(sms_features)[0]
    
    result = 'spam' if prediction == 'spam' else 'ham'
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
