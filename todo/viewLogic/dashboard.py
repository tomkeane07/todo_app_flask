# display username and to-do list
from flask.templating import render_template
import numpy as np
from flask.globals import request

to_do_list = ["AAAA", "BBB", "CCC"]

def render_dashboard(request):
    user=request.form["username"]
    render_template('dashboard/dashboard_main.html')
    

def get_to_do_list():
    return to_do_list