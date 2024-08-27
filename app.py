from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS
import socket

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

def list_all_addresses():
    # Get the hostname
    hostname = socket.gethostname()
    
    # Get the local IP address
    local_ip = socket.gethostbyname(hostname)
    
    # Get all network interfaces (this works for Unix-like systems)
    try:
        ip_list = socket.gethostbyname_ex(hostname)[2]
    except Exception as e:
        ip_list = [local_ip]

    return ip_list

if __name__ == '__main__':
    ip_list = list_all_addresses()
    print("Flask app running! You can access it using any of these addresses:")
    for ip in ip_list:
        print(f"http://{ip}:5000")
        
    app.run(host='0.0.0.0', port=5000) #Flask Server Configuration

