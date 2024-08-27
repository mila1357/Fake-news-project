from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


with open('./Model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('./tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    #Handle JSON Input for Predict Endpoint
    data  = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Input text not provided.'}), 400
    
    text = data['text']
    print(f"Input text: {text}")
    text_transformed = vectorizer.transform([text])
    prediction = model.predict(text_transformed)[0]
    print(f"Prediction: {prediction}")
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #Flask Server Configuration

