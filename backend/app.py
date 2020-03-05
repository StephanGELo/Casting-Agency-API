import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS
import json

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth

ITEMS_PER_PAGE = 6

def paginate_items(request, list):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    formatted_items = [item for item in list]
    paginated_items = formatted_items[start:end]

    return paginated_items

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
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
    @app.route('/movies', methods=['GET'])
    def get_movies():
        try:
            movies = Movie.query.all()
            formatted_movies = [movie.short() for movie in movies]
            selected_movies = paginate_items(request, formatted_movies)

            return jsonify({
                "success": True,
                "movies": selected_movies
            })
        except Exception:
            abort(400)


    #---------------------------------------------------#
    # Endpoints for Movies
    #---------------------------------------------------#
    @app.route('/movies-details', methods=['GET'])
    @requires_auth("get:movies-details")
    def get_movies_details(token):
        movies = Movie.query.all()
        formatted_movies = [movie.detailed() for movie in movies]
        paginated_movies = paginate_items(request, formatted_movies)
        
        for movie in paginated_movies:
            movie['actors'] = [actor.detailed() for actor in movie['actors']]

        try:
            return jsonify({
                "success": True,
                "movies": paginated_movies
            })
        except Exception:
            abort(422)
        
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth("delete:movies")
    def delete_a_movie(token, movie_id):
        movie = Movie.query.get(movie_id)

        try:
            movie.delete()
           
            return jsonify({
                "success": True,
                "deleted_movie": movie_id
            }), 200
        except Exception:
            abort(404)

    @app.route('/movies', methods=['POST'])
    @requires_auth("post:movies")
    def add_a_movie(token):
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        try:
           new_movie = Movie(title=new_title, release_date=new_release_date)
           new_movie.insert()
           return jsonify({
               "success": True,
               "added_movie": [new_movie.short()]
            }), 200
        except Exception:
            abort(400)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth("patch:movies")
    def update_a_movie(token, id):
        movie = Movie.query.get(id)

        if movie is None:
            abort(404)

        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        movie.title = new_title
        movie.release_date = new_release_date
        movie.update()
        updated_movie = [Movie.query.get(id).short()]

        return jsonify({
            "success": True,
            "updated_movie":[updated_movie]
        })
        
    #---------------------------------------------------#
    # Endpoints for Actors
    #---------------------------------------------------#
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()
        # paginated_actors = paginate_items(request, actors)
        formatted_actors = [actor.short() for actor in actors]
        selected_actors = paginate_items(request, formatted_actors)
        try:
            return jsonify({
                "success": True,
                "actors": selected_actors
            })
        except Exception:
            abort(422)
    
    @app.route('/actors-details', methods=['GET'])
    @requires_auth("get:actors")
    def get_actors_details(token):
        actors = Actor.query.all()
        # paginated_actors = paginate_items(request, actors)

        formatted_actors = [actor.detailed() for actor in actors]
        paginated_actors = paginate_items(request, formatted_actors)
        
        try:
            return jsonify({
                "success": True,
                "actors": paginated_actors
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth("delete:actors")
    def delete_an_actor(token, id):
        actor = Actor.query.get(id)
        try:
            actor.delete()

            return jsonify({
                "success": True,
                "deleted_actor": actor.short()
            })
        except Exception:
            abort(404)

    @app.route('/actors', methods=['POST'])
    @requires_auth("post:actors")
    def add_an_actor(token):
        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_movie = body.get('movie', None)

        try:
            new_actor = Actor(
                name=new_name,
                age=new_age,
                gender=new_gender,
                movie=new_movie
            )

            new_actor.insert()
            actor = Actor.query.get(new_actor.id).detailed()    

            return jsonify({
                "success": True,
                "added_actor": [actor]
            })
        except Exception:
            abort(400)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth("patch:actors")
    def update_actor(token, id):
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)

        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_movie = body.get('movie', None)

        actor.name = new_name
        actor.age = new_age
        actor.gender = new_gender
        actor.new_movie = new_movie
        actor.update()
        updated_actor = [Actor.query.get(id).detailed()]

        return jsonify({
            "success": True,
            "updated_actor":[updated_actor]
        })
    #---------------------------------------------------#
    # Error handlers
    #---------------------------------------------------#
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unauthorized'
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500
    
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app