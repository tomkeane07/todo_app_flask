from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.core import SelectField, StringField
from wtforms.validators import Length, InputRequired
from ....db.helpers.listDBHelper import seed_list
from flask import session
from flask.templating import render_template
from .main_list import add_itemForm



todo_list1 = ["AAAA", "BBB", "CCC"]
todo_list2 = ["DD", "EE", "FF"]

my_lists = [(todo_list1, "mylist1"), (todo_list2, "mylist2")]

def choose_list(request):
    if request.method == 'POST':
        list_choice = request.args.get("choose_list")

class Chooselist_dropdown(Form, list):
    choose_list = SelectField(u'', choices = my_lists)
    chooselist_btn = SubmitField("Choose List")
    
class Add_ListForm(Form):
    title = StringField(
        '',
        validators=[
            InputRequired(),
            Length(min=3, max=20)
        ],
        render_kw={
            "placeholder": "new list title...",
        }
    )
    add_list = SubmitField('Add List')

def handle_list_req(request):
    title = request.form.get("title")
    user_id = session['user']['id']
    print("_________")
    print(title)
    print(user_id)
    if request.method == 'POST':
        seed_list(title=title, user_id=user_id)
        return render_template(
        'logged_in/main_dashboard.html',
        main_list_title=my_lists[0][1],
        main_list=my_lists[0][0],
        username="kk",
        Add_ListForm=Add_ListForm(),
        chooselist_dropdown=Chooselist_dropdown(),
        add_itemForm=add_itemForm()
    )