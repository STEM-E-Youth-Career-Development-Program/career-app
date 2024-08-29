from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('html/home.html')

@app.route('/about')
def about():
    return render_template('html/about.html')

@app.route('/jobs')
def jobs():
    return render_template('html/jobs.html')

@app.route('/economy')
def economy():
    return render_template('html/economy.html')

@app.route('/contact')
def contact():
    return render_template('html/contact.html')

@app.route('/chat')
def chat():
    return render_template('html/chat.html')


if __name__ == '__main__':
    app.run(debug=True)