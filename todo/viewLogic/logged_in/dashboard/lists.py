from typing import List
from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.core import SelectField

todo_list1 = ["AAAA", "BBB", "CCC"]
todo_list2 = ["DD", "EE", "FF"]

my_lists = [(todo_list1, "mylist1"), (todo_list2, "mylist2")]

class Chooselist_dropdown(Form, list):
    choose_list = SelectField(u'choose list', choices = my_lists)
    chooselist_btn = SubmitField("click here to choose a to-do list")

def choose_list(request):
    if request.method == 'POST':
        list_choice = request.args.get("choose_list")