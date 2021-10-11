from flask import Flask, request 

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_page():
    return show_the_login_form()

@app.route('/login', methods=['POST'])
def login():
    return do_the_login()

def do_the_login():
    return 'Do the login'

def show_the_login_form():
    return 'Show the login form'


