import pickle
from flask import Flask, request

app = Flask(__name__)

with open('sentiment_model_v1.pkl', 'rb') as fp:
  model = pickle.load(fp)

@app.route("/")
def health():
    return {"message": "alive"}

@app.route('/api', methods=['POST'])
def sentiment_api():
  prompt = request.json['sentiment']
  prediction = model.predict([prompt])

  return {'sentence': prompt, "sentiment": prediction[0]}