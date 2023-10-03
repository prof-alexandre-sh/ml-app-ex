from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Carregue o modelo treinado (usaremos um modelo de regressão linear simples como exemplo)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def hello_world():
    return 'API de modelo treinado usando Flask'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
