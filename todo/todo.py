from flask import Flask
from .db.schemas import db
from .app.routes import set_routes
from .app.Config import ConfigClass
from flask_bootstrap import Bootstrap
from .db.schemas import db

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')
db.init_app(app)
set_routes(app)
Bootstrap(app)