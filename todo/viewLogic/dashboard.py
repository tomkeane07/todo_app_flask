# display username and to-do list
from flask.globals import request
from flask.templating import render_template
from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.core import SelectField

todo_list1 = ["AAAA", "BBB", "CCC"]
todo_list2 = ["DD", "EE", "FF"]

my_lists = [(todo_list1, "mylist1"), (todo_list2, "mylist2")]

def dashboard_request_handler(request):
    username = request.args.get("username")
    if request.method == 'GET':
        return render_dashboard(username)

def render_dashboard(username):
    return render_template(
        'logged_in/main_dashboard.html',
        todo_list=my_lists[0][0],
        username=username,
        list_options=list_options()
    )
    

#def

# class todo_list_view(my_lists):

class list_options(Form):
    choose_list = SelectField(u'choose list', choices = my_lists)
    chooselist_btn = SubmitField("click here to choose a to-do list")
