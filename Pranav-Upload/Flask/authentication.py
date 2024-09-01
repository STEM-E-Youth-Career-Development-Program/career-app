# Firebase authentication
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCsfQbZCtAZaYAD2eENvysZbxTW-aE7bUw",
    "authDomain": "career-app-35794.firebaseapp.com",
    "projectId": "career-app-35794",
    "storageBucket": "career-app-35794.appspot.com",
    "messagingSenderId": "593679880557",
    "appId": "1:593679880557:web:34a040cdcb29e2274b4a64",
    "measurementId": "G-H7VL9PY3T0",
    "databaseURL": "https://career-app-35794-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#login
email = input("Enter your email: ")
password = input("Enter your password: ")


def register(email,password):
    user = auth.create_user_with_email_and_password(email, password)
    auth.send_email_verification(user["idToken"])

def signIn(email,password):
    try:
        auth.sign_in_with_email_and_password(email, password)
    except:
        return "Failed to login"

def resetPassword(email):
    auth.send_password_reset_email(email)
