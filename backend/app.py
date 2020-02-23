import os
from flask import Flask
from flask_cors import CORS
from backend.models import setup_db

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_movies():
        return "I'm deployed!! Bring on all your movies now"
        
    return app