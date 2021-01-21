from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.core import StringField

    
class add_itemForm(Form):
    item = StringField(' add item', render_kw={
        "placeholder": "task description...",
    })
    add_item = SubmitField()

