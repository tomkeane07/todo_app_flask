# display username and to-do list
from flask.globals import request, session
from flask.templating import render_template
from .lists import Chooselist_dropdown
from ....db.helpers.UserDbHelper import getUser_byUsername_asDict
from flask import session


todo_list1 = ["AAAA", "BBB", "CCC"]
todo_list2 = ["DD", "EE", "FF"]

my_lists = [(todo_list1, "mylist1"), (todo_list2, "mylist2")]

def dashboard_request_handler(request):
    username = request.args.get("username")
    if request.method == 'GET':
        return render_dashboard(username)

def render_dashboard(username, lists=None):
    session['user'] = getUser_byUsername_asDict(username)
    return render_template(
        'logged_in/main_dashboard.html',
        todo_list=my_lists[0][0],
        username=username,
        chooselist_dropdown=Chooselist_dropdown()
    )