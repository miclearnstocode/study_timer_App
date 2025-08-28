from flask import Flask
from database.connection import DatabaseConnection
from routes.user_routes import user_bp
from routes.timer_routes import timer_bp
from routes.session_routes import session_bp

def create_app():
    app = Flask(__name__)

    # Initialize database
    db = DatabaseConnection()
    db.initialize()

    # Register blueprints
    app.register_blueprint(session_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(timer_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
