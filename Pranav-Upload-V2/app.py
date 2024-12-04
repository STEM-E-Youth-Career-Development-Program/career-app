from flask import Flask, render_template # type: ignore
app = Flask(__name__)

@app.route('/')
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

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    
    # sign up data - for now getting printed but should be saved to a database
    print(f"Username: {username}, Password: {password}")
    
    return redirect(url_for('success'))

# Success route to show after signup
@app.route('/success')
def success():
    return "Signup successful!"

if __name__ == '__main__':
    app.run(debug=True)
