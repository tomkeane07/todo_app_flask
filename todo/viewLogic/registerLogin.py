from flask import Flask, render_template, url_for
from werkzeug.utils import redirect
from ..db.UserDbHelper import user_exists, verify_user, seed_user

# route_helper

# Home

def handle_login(request):
    username = request.form['loginuser']
    password = request.form['loginpassword']
    if user_exists(username):
        if verify_user(username, password):
            message = 'logged in. \nWelcome "{username}"'.format(username=username)
            return login_user(message)
        else:
            error_msg='incorrect credentials'
            return render_template('registerlogin.html', message=error_msg)
    else:
        message='user "{username}" does not exist'.format(username=username)
        return render_template('logged_out/registerLogin.html', message=message)

def handle_register(request):
    username = request.form['registerusername']
    password = request.form['registerpassword']
    if user_exists(username):
        message = "user '{username}' already exists".format(username=username)
        return render_template('logged_out/registerlogin.html', message=message)
    else:
        seed_user(username, password)
        message = 'Account created for "{username}"'.format(username=username)
        return login_user(message)
        
def login_user(message):
    return redirect(url_for('dashboard'))

def render_register_login():
    return render_template('logged_out/registerlogin.html', message='please register or log in')