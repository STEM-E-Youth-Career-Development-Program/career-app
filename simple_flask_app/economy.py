from flask import Flask, render_template
import requests

app = Flask(__name__)

# FRED API Key and Endpoint
API_KEY = '3d92d94931795c1e125e3229b4ad7efc'  #  FRED API key
FRED_ENDPOINT = 'https://api.stlouisfed.org/fred/series/observations'
SERIES_ID = 'UNRATE'  # Example: U.S. Unemployment Rate

def fetch_fred_data():
    """Fetch the latest 5 observations from the FRED API."""
    try:
        response = requests.get(
            FRED_ENDPOINT,
            params={
                'series_id': SERIES_ID,
                'api_key': API_KEY,
                'file_type': 'json'
            }
        )
        data = response.json()
        return data['observations'][-5:]  # Get the last 5 observations
    except Exception as e:
        print(f"Error fetching FRED data: {e}")
        return []  # Return an empty list if there's an error

@app.route('/economy')
def economy():
    economic_data = fetch_fred_data()
    return render_template('economy.html', economic_data=economic_data)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
