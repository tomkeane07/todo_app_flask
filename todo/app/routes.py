from flask import request
from ..viewLogic.dashboard import dashboard_request_handler
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
        return handle_login(request)

    @app.route('/registeruser', methods=['POST'])
    def registeruser():
        return handle_register(request)

    @app.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return dashboard_request_handler(request)

    @app.route('/privacypolicy', methods=['GET'])
    def privacyPolicy():
        return render_privacypolicy()
    
    @app.route('/tasks', methods=['GET', 'POST', 'REMOVE'])
    def tasks():
        return #handle_tasks_db_req(request)

