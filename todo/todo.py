from flask import Flask
from .db.schemas import db
from .routes.router import init_routes
from .app.Config import ConfigClass
from flask_bootstrap import Bootstrap
from .db.schemas import db

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')
db.init_app(app)
init_routes(app)
Bootstrap(app)