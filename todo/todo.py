from flask import Flask
from .db.schemas import init_schemas
from .app.routes import set_routes
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'
set_routes(app)
init_schemas()
Bootstrap(app)