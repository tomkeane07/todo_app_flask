import sqlite3
from flask_user import login_required, UserManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

def init_dbs(app):
    db = SQLAlchemy(app)

    class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
        # User authentication information. The collation='NOCASE' is required
        # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
        username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
    
    class Lists(db.Model):
        __tablename__ = 'lists'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
        title = db.Column(db.String(100), nullable=False)

    class Tasks(db.Model):
        __tablename__ = 'tasks'
        id = db.Column(db.Integer, primary_key=True)
        list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
        description = db.Column(db.String(200), nullable=False)

    db.create_all()

    user_manager = UserManager(app, db, User)