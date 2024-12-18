import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

file_path = '../data/sms_dataset.csv'
df = pd.read_csv(file_path)

stop_words = set(stopwords.words('arabic') + stopwords.words('french'))
df['message'] = df['message'].str.lower().str.replace('[^\w\s]', '')
df['message'] = df['message'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

X = df['message']
y = df['label']

vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

joblib.dump(model, '../train/sms_spam_classifier.pkl')
joblib.dump(vectorizer, '../train/tfidf_vectorizer.pkl')
print("Model and vectorizer saved successfully.")
