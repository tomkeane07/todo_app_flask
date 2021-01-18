from flask import Flask
from .db.schemas import init_dbs
from .app.routes import set_routes
from .app.Config import ConfigClass
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')
set_routes(app)
init_dbs(app)
Bootstrap(app)