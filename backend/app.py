import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
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
    # CORS(app)
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
        paginated_movies = paginate_items(request, movies)
        try:
            return jsonify({
                "success": True,
                "movies": paginated_movies
            })
        except Exception:
            abort(422)
        
    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_a_movie(id):
        movie = Movie.query.get(id)
        try:
            movie.delete()

            return jsonify({
                "success": True,
                "deleted": movie.format()
            })
        except Exception:
            abort(404)
    
    # @app.route('/movies', methods=['POST'])
    # def add_a_movie():
    #     data = request.get_json()

    #     new_title = data.title
    #     new_release_date = data.release_date

    #     try:
    #         movie = Movie(
    #             title=new_title,
    #             release_date=new_release_date
    #         )

    #         movie.insert()
    #         return jsonify(
    #             'success': True
    #         )
    #     except Exception:
    #         abort(422)


    return app

        