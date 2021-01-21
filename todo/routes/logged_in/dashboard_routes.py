from flask import request
from ...viewLogic.logged_in.dashboard.dashboard import dashboard_request_handler
from ...viewLogic.logged_in.dashboard.list_options import choose_list


def set_dashboard_routes(app):
    @app.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return dashboard_request_handler(request)

    @app.route('/dashboard/chooselist', methods=['POST', 'GET'])
    def dashchoose_List():
        return choose_list(request)

