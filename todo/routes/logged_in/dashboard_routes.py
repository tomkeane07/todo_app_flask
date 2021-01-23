from flask import request
from ...viewLogic.logged_in.dashboard.dashboard import dashboard_request_handler
from ...viewLogic.logged_in.dashboard.list_options import choose_mainlist, add_list
from ...viewLogic.logged_in.dashboard.main_list import add_item, delete_task

def set_dashboard_routes(app):
    @app.route('/dashboard', methods=['GET', 'POST'])
    def dashboard():
        return dashboard_request_handler(request)

    # list options

    @app.route('/dashboard/listoptions/chooselist', methods=['POST', 'GET'])
    def listoptions_choosemainlist():
        return choose_mainlist(request)
    
    @app.route('/dashboard/listoptions/add_list', methods=['POST'])
    def listoptions_addlist():
        return add_list(request)

    # main list

    @app.route('/dashboard/mainlist/add_task', methods=['POST'])
    def mainlist_additem():
        return add_item(request)

    @app.route('/dashboard/mainlist/delete_task', methods=['POST'])
    def mainlist_delete_task():
        return delete_task(request)
    
    @app.route('/dashboard/mainlist/delete_list', methods=['POST'])
    def mainlist_delete_list():
        return delete_task(request)