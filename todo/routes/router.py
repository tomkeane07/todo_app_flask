from .logged_in.dashboard_routes import set_dashboard_routes
from .logged_out.landing_routes import set_landing_routes

def init_routes(app):
    set_dashboard_routes(app)
    set_landing_routes(app)