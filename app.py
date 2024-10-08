from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


with open('ML/Model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('ML/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')
    if text is not None:
        text_transformed = vectorizer.transform([text])

        prediction = model.predict(text_transformed)[0]

        return jsonify({'prediction': int(prediction)})
    else:
        return jsonify({'error': 'Input text not provided.'})

if __name__ == '__main__':
    app.run(debug=True)
