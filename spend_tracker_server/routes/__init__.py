from .dashboard_routes import dashboard_bp
from .statement_routes import statement_bp
# from .transaction_routes import transaction_bp
# from .insight_routes import insight_bp

def register_routes(app):
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(statement_bp)
    # app.register_blueprint(transaction_bp)
    # app.register_blueprint(insight_bp)