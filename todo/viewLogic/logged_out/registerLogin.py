from flask import render_template, url_for
from werkzeug.utils import redirect
from ...db.helpers.userDbHelper import user_exists, verify_user, seed_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, InputRequired
from flask_wtf import FlaskForm

# route_helper

# Home

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=10)])
    registerBtn = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=10)])
    loginBtn = SubmitField("Log in")

def render_register_login(
    message='please register or log in'
):  return render_template(
        'logged_out/registerlogin.html',
        message=message,
        LoginForm=LoginForm(),
        RegisterForm=RegisterForm()
    )

def handle_register(request):
    username=request.form.get('username')
    password=request.form.get('password')
    if user_exists(username):
        message = "user '{username}' already exists".format(username=username)
        return render_register_login(message=message)
    else:
        seed_user(username, password)
        message = 'Account created for "{username}"'.format(username=username)
        return login_user(username=username, message=message)

def handle_login(request):
    username=request.form.get('username')
    password=request.form.get('password')
    if user_exists(username):
        if verify_user(username, password):
            message = 'logged in. \nWelcome "{username}"'.format(username=username)
            return login_user(username, message)
        else:
            error_msg='incorrect credentials'
            return render_template('registerlogin.html', message=error_msg)
    else:
        message='user "{username}" does not exist'.format(username=username)
        return render_template('logged_out/registerLogin.html', message=message)


def login_user(username, message=""):
    return redirect(url_for('dashboard', message=message, username=username))