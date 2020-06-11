from flask import Flask

from api.controller import prediction_app


def create_app() -> Flask:
    """Create a flask app instance."""
    
    flask_app = Flask('ml_api')
    
    flask_app.register_blueprint(prediction_app)
    
    return flask_app
