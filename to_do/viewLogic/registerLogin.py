from flask import Flask, render_template, request
from ..usersDB.UserDbHelper import user_exists, verify_user, seed_user

# route_helper

# Home

def login_user(request):
    username = request.form['loginuser']
    password = request.form['loginpassword']
    if user_exists(username):
        if verify_user(username, password):
            message = 'logged in \nWelcome "{username}"'.format(username=username)
            return render_template('dashboard/main_dashboard.html', message= message)
        else:
            error_msg='incorrect credentials'
            return render_template('registerlogin.html', message=error_msg)
    else:
        message='user "{username}" does not exist'.format(username=username)
        return render_template('dashboard/main_dashboard.html', message=message)

def register_user(request):
    username = request.form['registerusername']
    password = request.form['registerpassword']
    if user_exists(username):
        message = "user '{username}' already exists".format(username=username)
        return render_template('registerlogin.html', message=message)
    else:
        seed_user(username, password)
        message = 'Account created for "{username}"'.format(username=username)
        return render_template('dashboard/main_dashboard.html', message=message)

def render_register_login():
    return render_template('registerlogin.html', message='Welcome')
