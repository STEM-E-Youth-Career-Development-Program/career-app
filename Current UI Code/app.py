import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
import google.generativeai as genai
import markdown2

load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
my_api_key_gemini = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=my_api_key_gemini)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="tunedModels/career-hihylynnt54i",
    generation_config=generation_config,
)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/economy')
def economy():
    return render_template('economy.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        try:
            response = model.generate_content(prompt)
            
            html_response = markdown2.markdown(response.text, extras=['tables', 'fenced-code-blocks', 'cuddled-lists'])
            
            return jsonify({
                'response': html_response
            })
        
        except Exception as e:
            return jsonify({
                'response': f"Sorry, something went wrong: {str(e)}"
            })
    
    return render_template('chat.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
   
    if email == 'test@example.com' and password == 'password':
        return redirect(url_for('home'))
    else:
        return redirect(url_for('welcome'))

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
