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
