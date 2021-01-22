# display username and to-do list
from flask.globals import session
from flask.templating import render_template
from .main_list import add_itemForm
from .list_options import Add_ListForm, Chooselist_dropdown
from ....db.helpers.userDbHelper import getUser_byUsername_asDict

todo_list1 = ["AAAA", "BBB", "CCC"]
todo_list2 = ["DD", "EE", "FF"]

my_lists = [(todo_list1, "mylist1"), (todo_list2, "mylist2")]

def dashboard_request_handler(request):
    username = request.args.get("username")
    if request.method == 'GET':
        return render_dashboard(username)

def render_dashboard(username):
    session['user'] = getUser_byUsername_asDict(username)
    return render_template(
        'logged_in/main_dashboard.html',
        main_list_title=my_lists[0][1],
        main_list=my_lists[0][0],
        username=username,
        Add_ListForm=Add_ListForm(),
        chooselist_dropdown=Chooselist_dropdown(),
        add_itemForm=add_itemForm()
    )