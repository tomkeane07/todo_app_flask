from flask import request
from ...viewLogic.logged_in.dashboard.dashboard import dashboard_request_handler
from ...viewLogic.logged_in.dashboard.list_options import choose_list, handle_list_req


def set_dashboard_routes(app):
    @app.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return dashboard_request_handler(request)

    @app.route('/dashboard/chooselist', methods=['POST', 'GET'])
    def choose_list():
        return choose_list(request)

    @app.route('/dashboard/todo_list', methods=['POST', 'GET'])
    def todo_list():
        return
    
    @app.route('/dashboard/add_list', methods=['POST'])
    def add_list():
        return handle_list_req(request)