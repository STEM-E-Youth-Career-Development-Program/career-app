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
email = ""
password = ""
def register(email, password):
    try:
        print("Attempting to register...")
        user = auth.create_user_with_email_and_password(email, password)
        print("Registration successful!")
        print("Sending verification email...")
        auth.send_email_verification(user["idToken"])
        print("Verification email sent!")
        return user
    except Exception as e:
        print(f"An error occurred during registration: {str(e)}")
        return None

def signIn(email, password):
    try:
        print("Attempting to sign in...")
        user = auth.sign_in_with_email_and_password(email, password)
        print("Sign in successful!")
        return user
    except Exception as e:
        print(f"Failed to login: {str(e)}")
        return None

def resetPassword(email):
    try:
        print("Sending password reset email...")
        auth.send_password_reset_email(email)
        print("Password reset email sent!")
    except Exception as e:
        print(f"Failed to send password reset email: {str(e)}")
