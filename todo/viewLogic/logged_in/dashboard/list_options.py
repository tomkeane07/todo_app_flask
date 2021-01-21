from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.core import SelectField, StringField
from wtforms.validators import Length, InputRequired

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
        validators=[InputRequired(),
        Length(min=3, max=20)],
        render_kw={
            "placeholder": "new list title...",
        }
    )
    add_list = SubmitField('Add List')
