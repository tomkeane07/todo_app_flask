# display username and to-do list
from flask.templating import render_template

todo_list = ["AAAA", "BBB", "CCC"]

def render_dashboard():
    return render_template('logged_in/main_dashboard.html', todo_list=todo_list)