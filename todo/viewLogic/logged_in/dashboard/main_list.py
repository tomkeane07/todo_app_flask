from flask.globals import session
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import StringField
from werkzeug.utils import redirect
from flask import url_for
from ....db.helpers.tasksDbHelper import seed_task, remove_task
from ....db.helpers.listDbHelper import remove_list

    
class add_itemForm(FlaskForm):
    description = StringField(' add item', render_kw={
        "placeholder": "task description...",
    })
    add_item = SubmitField()

def add_item(request):
    description = request.form.get("description")
    list_id = session['user']['main_list_id']
    seed_task(description=description, list_id=list_id)
    username = session['user']['username']
    return redirect(url_for('dashboard', message='', username=username))

def delete_task(request):
    remove_task(request.form.get("task_id"))
    return redirect(url_for('dashboard', message='', username=session['user']['username']))

def delete_list(request):
    remove_list(request.form.get("list_id"))
    return redirect(url_for('dashboard', message='', username=session['user']['username']))
