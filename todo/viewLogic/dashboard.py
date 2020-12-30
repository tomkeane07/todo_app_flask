# display username and to-do list
from flask.templating import render_template
import numpy as np
from flask.globals import request

todo_list = ["AAAA", "BBB", "CCC"]

def render_dashboard(request):
    user=request.form["username"]
    render_template('dashboard/dashboard_main.html', todo_list=todo_list)