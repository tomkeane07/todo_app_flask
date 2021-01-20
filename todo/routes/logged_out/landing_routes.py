from flask import request
from ...viewLogic.logged_out.registerLogin import handle_login, handle_register, render_register_login
from ...viewLogic.logged_out.about import render_about
from ...viewLogic.logged_out.privacypolicy import render_privacypolicy


def set_landing_routes(app):
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


    @app.route('/privacypolicy', methods=['GET'])
    def privacyPolicy():
        return render_privacypolicy()
