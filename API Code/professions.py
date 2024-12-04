from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


BLS_API_KEY = 'bd48bf64cc5248d9923dfa3fe1908219'
BLS_API_URL = 'https://api.bls.gov/publicAPI/v2/timeseries/data/CEU0000000001'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bls-data')
def get_bls_data():
    # Define parameters for the BLS API request
    params = {
        'bd48bf64cc5248d9923dfa3fe1908219': BLS_API_KEY
    }
    
    try:
        # Make the request to the BLS API
        response = requests.get(BLS_API_URL, params=params)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        # Extract relevant data
        if 'Results' in data and 'series' in data['Results']:
            series_data = data['Results']['series'][0]['data']
            return jsonify(series_data)  # Send data as JSON to the frontend

        return jsonify({'error': 'No data found'}), 404
    
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
