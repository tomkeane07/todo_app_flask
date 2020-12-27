from flask import Flask
from .db.schemas import init_users_db
from .app.routes import set_routes

app = Flask(__name__)
set_routes(app)
init_users_db()