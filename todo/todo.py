from flask import Flask
from .db.db import db
from .db.models.create_tables import create_tables
from .routes.router import init_routes
from flask_bootstrap import Bootstrap
from .app.Config import ConfigClass

app = Flask(__name__)
app.config.from_object(ConfigClass)
db.init_app(app)
init_routes(app)
create_tables(app, db)
Bootstrap(app)