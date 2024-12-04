import firebase_admin
from firebase_admin import credentials
import pyrebase
from flask import Flask, session, rendertemplate, request, redirect

app = Flask(__name__)

cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT_ID.firebaseapp.com",
    "databaseURL": "https://your_project_id.firebaseio.com/",
    "projectId": "YOUR_PROJECT_ID",
    "storageBucket": "YOUR_PROJECT_ID.appspot.com",
    "messagingSenderId": "YOUR_SENDER_ID",
    "appId": "YOUR_APP_ID",
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Login successful")
        session['user'] = email
        return render_template('home.html')
    except Exception as e:
        print(f"Failed to login: {e}")
        return f"Failed to login"

@app.route('/login', methods=['POST','GET'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    result = sign_in(email, password)

if __name__ == '__main__':
    app.run(debug=True)
