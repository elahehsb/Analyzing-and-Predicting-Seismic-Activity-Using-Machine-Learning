from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('models/seismic_activity_prediction_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    depth = data['depth']
    magnitude = data['magnitude']

    # Prepare input data
    input_data = pd.DataFrame([[latitude, longitude, depth, magnitude]], columns=['latitude', 'longitude', 'depth', 'mag'])

    # Make prediction
    prediction = model.predict(input_data)
    return jsonify({'significant_earthquake': bool(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
