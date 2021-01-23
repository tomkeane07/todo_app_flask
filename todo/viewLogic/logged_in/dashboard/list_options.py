from werkzeug.utils import redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import SelectField, StringField
from wtforms.validators import Length, InputRequired
from ....db.helpers.userDbHelper import set_users_main_list
from ....db.helpers.listDbHelper import seed_list_and_return_list_id, get_users_lists_as_list_tuples
from .main_list import add_itemForm
from flask import session, url_for
from flask.templating import render_template

todo_list1 = ["AAAA", "BBB", "CCC"]
todo_list2 = ["DD", "EE", "FF"]

my_lists = [(todo_list1, "mylist1"), (todo_list2, "mylist2")]

class Chooselist_dropdown(FlaskForm):
    list_choice = SelectField(u'', coerce=int)
    chooselist_btn = SubmitField("Choose Main List")
    
class Add_ListForm(FlaskForm):
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

def add_list(request):
    title = request.form.get("title")
    user_id = session['user']['id']
    new_list_id = seed_list_and_return_list_id(title=title, user_id=user_id)
    username = session['user']['username']
    update_user_main_list(user_id, new_list_id)
    return redirect(url_for('dashboard', message='', username=username))

def choose_mainlist(request):
    user_id = session['user']['id']
    get_users_lists_as_list_tuples(user_id)
    if request.method == 'POST':
        chosen_list_id = request.form.get("list_choice")
        username = session['user']['username']
        update_user_main_list(user_id, chosen_list_id)
        return redirect(url_for('dashboard', message='', username=username))

def update_user_main_list(user_id, new_list_id):
    set_users_main_list(user_id, new_list_id)
