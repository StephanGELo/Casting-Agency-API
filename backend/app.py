import os
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import json

from backend.models import setup_db, Movie, Actor

ITEMS_PER_PAGE = 6

def paginate_items(request, list):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    formatted_items = [item.format() for item in list]
    paginated_items = formatted_items[start:end]

    return paginated_items

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    CORS(app, resources={r"/api/": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, DELETE, PATCH'
        )
        return response


    #-------------------------------------------------------#
    # ROUTES
    #-------------------------------------------------------#

    #--------------------#
    # Movies
    #--------------------#

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]

        return jsonify({
            "success": "True",
            "movies": formatted_movies
        })
        
    return app