from flask import request
from werkzeug.utils import redirect
from ..viewLogic.dashboard import render_dashboard, handle_post
from ..viewLogic.registerLogin import handle_login, handle_register, render_register_login
from ..viewLogic.about import render_about
from ..viewLogic.privacypolicy import render_privacypolicy


def set_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        if request.method == 'GET':
            return render_register_login()

    @app.route('/about', methods=['GET'])
    def about():
        return render_about()

    @app.route('/loginuser', methods=['POST'])
    def loginuser():
        if request.method == 'POST':
            return handle_login()

    @app.route('/registeruser', methods=['POST'])
    def registeruser():
        if request.method == 'POST':
            return handle_register()

    @app.route('/dashboard', methods=['GET', 'POST'], subdomain="<username>")
    def dashboard():
        if request.method == 'GET':
            return render_dashboard(request)
        
        if request.method == 'POST':
            return handle_post(request)

    @app.route('/privacypolicy', methods=['GET'])
    def privacyPolicy():
        return render_privacypolicy()
    
    @app.route('/tasks', methods=['GET', 'POST', 'REMOVE'])
    def tasks():
        return #handle_tasks_db_req(request)

