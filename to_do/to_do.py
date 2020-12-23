from flask import Flask, request
from .viewLogic.registerLogin import login_user, register_user, render_register_login
from .viewLogic.about import render_about

app = Flask(__name__)

#Router
@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_register_login()

@app.route('/about', methods=['GET'])
def about():
    return render_about()

@app.route('/loginuser', methods=['POST'])
def loginuser():
    if request.method == 'POST':
        return login_user(request)

@app.route('/registeruser', methods=['POST'])
def registeruser():
    if request.method == 'POST':
        return register_user(request)