Tunsian SMS Spam Detection API
======================

This project provides a Python API for classifying SMS messages as spam or ham (not spam). The model has been pre-trained using a dataset of Tunisian SMS messages. If you wish to add your own datasets and retrain the model, follow the instructions below.

Table of Contents
-----------------

*   [Prerequisites](#prerequisites)
*   [Installation](#installation)
*   [How to Use the API](#how-to-use-the-api)
*   [Retrain the Model](#retrain-the-model)
*   [API Endpoints](#api-endpoints)
*   [Contributing](#contributing)
*   [License](#license)

Prerequisites
-------------

*   Python 3.x
*   Virtual environment (recommended)

Installation
------------

1.  **Clone the repository:**
   `git clone https://github.com/mahdibenabd/Tunisian_SMS_spam_classifier_API.git`  
`cd Tunisian_SMS_spam_classifier_API`

2.  **Set up the virtual environment:** 

    `python -m venv env`  
    `source env/bin/activate`
3.  **Install the required packages:**

    `pip install -r requirements.txt`

How to Use the API
------------------

1.  **Start your Python API server:**
   `cd predict`
   `python predict_sms.py`  

This command will start your Flask API server.

2.  **From your Android app, send a POST request to the API to predict if an SMS is spam or not:**  

    `POST http://127.0.0.1:5000/predict_sms`  
    `Content-Type: application/json`  
    `{ "sms": "Your SMS content here" }`  
 Replace "Your SMS content here" with the actual SMS text.

3.  **Response:** The API will respond with a JSON object containing:  

    `{ "result": "spam" }`

Retrain the Model
-----------------

To retrain the model with your own datasets, follow these steps:

1. **Prepare your dataset:**  

   Place your dataset CSV files in the `data/` directory. The file should have thre columns: `id ` ,`message` and `label` (e.g., "spam" or "ham").  
   Example CSV:  
    `id,message,label`  
    `42785,شرجي خطك و ادخل في القرعة فما 25 مليون كاش مجانية.,spam`  
    `42786,ألو وينك؟ نستنى فيك في القهوة,ham`
2.  **Retrain the model:** 
   Run the following command to retrain your model:  
    `python retrain_model.py`  
   This script will:
   - Load your dataset from `datasets/`.
   - Preprocess the data (tokenization, padding, etc.).
   - Train the model.
   - Save the trained model as `sms_spam_classifier.pkl`.
3. **Update the API with the new model:**  
   - Modify your `predict_sms.py` file to load the new model:  
      `from joblib import load`  
      `model = load('model.pkl')`

API Endpoints
-------------

*   **POST /predict\_sms**: Predict if an SMS is spam or not.
    *   Request: JSON object with `sms` field (string).
    *   Response: JSON object with `result` field ("spam" or "ham").
*   **Example Request from Android App**  
   - To send a request from your Android app, use the following code snippet in your Android app:  
    `OkHttpClient client = new OkHttpClient(); 
    MediaType JSON = MediaType.parse("application/json; charset=utf-8");
    RequestBody body = RequestBody.create(
        "{ \"sms\": \"ربحت معانا\" }",
         JSON );
    Request request = new Request.Builder()
      .url("http://127.0.0.1:5000/predict_sms")
       .post(body) 
       .addHeader("Content-Type", "application/json") 
       .build();
      try (Response response = client.newCall(request).execute()){ 
         if (response.isSuccessful()) {
             String responseBody = response.body().string();
             System.out.println("Response: " + responseBody); 
              } else {
                  System.out.println("Request failed: " + response.code()); 
                  } } catch (IOException e) { e.printStackTrace();
                   }`

Contributing
------------

   1.  **Fork this repository**
2.  **Create your feature branch (\`git checkout -b feature-branch\`)**
3.  **Commit your changes (\`git commit -am 'Add new feature'\`)**
4.  **Push to the branch (\`git push origin feature-branch\`)**
5.  **Create a new Pull Request**
