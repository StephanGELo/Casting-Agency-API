import os, sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from flask_cors import CORS
import json

from .models import setup_db, Movie, Actor
from .auth import AuthError, requires_auth

script_dir = sys.path[0]

ITEMS_PER_PAGE = 10

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
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Origins',
            '*'
        )    
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, True'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, DELETE, PATCH'
        )
        return response


# -------------------------------------------------------#
# ROUTES
# -------------------------------------------------------#
    # ---------------------------------------------------#
    # Endpoints for index page
    # ---------------------------------------------------#

    @app.route('/movies', methods=['GET'])
    def get_movies():
        try:
            movies = Movie.query.order_by(Movie.created).all()
            formatted_movies = [movie.format() for movie in movies]
            selected_movies = paginate_items(request, formatted_movies)

            if len(selected_movies) == 0:
                abort(404)
            
            for movie in selected_movies:
                movie['actors'] = [actor.get_name()
                                   for actor in movie['actors']]   
      

            return jsonify({
                "success": True,
                "movies": selected_movies,
                "total_movies": len(formatted_movies)
            })
        except Exception:
            abort(404)

    @app.route('/actors', methods=['GET'])
    def get_actors():
        try:
            actors = Actor.query.order_by(Actor.id).all()
            formatted_actors = [actor.format() for actor in actors]
            selected_actors = paginate_items(request, formatted_actors)

            if len(selected_actors) == 0:
                abort(404)

            return jsonify({
                "success": True,
                "actors": selected_actors,
                "total_actors": len(formatted_actors)
            })
        except Exception:
            abort(404)

    # ---------------------------------------------------#
    # Endpoints for Movies
    # ---------------------------------------------------#
    @app.route('/movies-details', methods=['GET'])
    @requires_auth("get:movies-details")
    def get_movies_details(token):
        try:
            movies = Movie.query.order_by(Movie.id).all()
            formatted_movies = [movie.format() for movie in movies]
            paginated_movies = paginate_items(request, formatted_movies)

            if len(paginated_movies) == 0:
                abort(404)

            for movie in paginated_movies:
                movie['actors'] = [actor.get_name()
                                   for actor in movie['actors']]

            return jsonify({
                "success": True,
                "movies": paginated_movies,
                "total_movies": len(formatted_movies)
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth("delete:movies")
    def delete_a_movie(token, movie_id):
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        try:
            movie.delete()

            return jsonify({
                "success": True,
                "deleted_movie": [movie.format()]
            }), 200
        except Exception:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth("post:movies")
    def add_a_movie(token):
        try:
            body = request.get_json()
            new_title = body['title']
            new_release_date = body['release_date']
            new_image_link = body['image_link']

            if len(new_title) == 0:
                abort(400)
            elif len(new_release_date) == 0:
                abort(400)
            elif len(new_image_link) == 0:
                new_image_link = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRhivZm-siBHym-ABcIaglDFgag9D-EAxzbDUwBU2XDjm027LSa&usqp=CAU'

            new_movie = Movie(
                title=new_title, 
                release_date=new_release_date, 
                image_link=new_image_link
            )

            new_movie.insert()
            movie = Movie.query.get(new_movie.id).format()

            return jsonify({
                "success": True,
                "added_movie": [movie]
            }), 200
        except Exception:
            abort(400)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth("patch:movies")
    def update_a_movie(token, movie_id):
        try:
            movie = Movie.query.get(movie_id)

            if movie is None:
                abort(404)

            body = request.get_json()
            new_title = body.get('title', None)
            new_release_date = body.get('release_date', None)
            new_image_link = body.get('image_link', None)

            if len(new_title) == 0:
                abort(422)
            elif len(new_release_date) == 0:
                abort(422)
            elif len(new_image_link) == 0:
                new_image_link = os.path.join(script_dir, '../frontend/public/no_movie_poster.jpeg')

            movie.title = new_title
            movie.release_date = new_release_date
            movie.image_link = new_image_link
            movie.update()
            updated_movie = [Movie.query.get(movie_id).format()]

            return jsonify({
                "success": True,
                "added_movie": [updated_movie]
            })
        except Exception:
            abort(422)

    # ---------------------------------------------------#
    # Endpoints for Actors
    # ---------------------------------------------------#
    @app.route('/actors-details', methods=['GET'])
    @requires_auth("get:actors-details")
    def get_actors_details(token):
        try:
            actors = Actor.query.order_by(Actor.id).all()
            formatted_actors = [actor.format() for actor in actors]
            paginated_actors = paginate_items(request, formatted_actors)

            if len(paginated_actors) == 0:
                abort(404)

            return jsonify({
                "success": True,
                "actors": paginated_actors,
                "total_actors": len(formatted_actors)
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth("delete:actors")
    def delete_an_actor(token, id):
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)

        try:
            actor.delete()

            return jsonify({
                "success": True,
                "deleted_actor": actor.format()
            })
        except Exception:
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth("post:actors")
    def add_an_actor(token):
        try:
            body = request.get_json()
            print("body is :", body)

            new_name = body['name']
            new_age = int(body['age'])
            new_gender = body['gender']
            new_image_link = body['image_link']
            new_movie = body['movie']

            if len(new_name) == 0:
                abort(400)
            elif new_age == 0:
                abort(400)
            elif len(new_gender) == 0:
                abort(400)
            elif len(new_image_link) == 0:
                new_image_link = os.path.join(script_dir, '../frontend/public/logo192.png')        

        
            new_actor = Actor(
                name=new_name,
                age=new_age,
                gender=new_gender,
                image_link=new_image_link,
                movie=new_movie
            )

            new_actor.insert()
            actor = Actor.query.get(new_actor.id).format()

            return jsonify({
                "success": True,
                "added_actor": [actor]
            })
        except Exception:
            abort(400)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth("patch:actors")
    def update_actor(token, actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_image_link = body.get('image_link', None)
        new_movie = body.get('movie', None)

        if len(new_name) == 0:
            abort(422)
        elif new_age == 0:
            abort(422)
        elif len(new_gender) == 0:
            abort(422)
        elif len(new_image_link) == 0:
            new_image_link = os.path.join(script_dir, '../frontend/public/logo192.png')

        try:
            actor.name = new_name
            actor.age = new_age
            actor.gender = new_gender
            actor.image_link = new_image_link
            actor.new_movie = new_movie

            actor.update()
            updated_actor = [Actor.query.get(actor_id).format()]

            return jsonify({
                "success": True,
                "updated_actor": [updated_actor]
            }), 200
        except Exception:
            abort(422)

    # ---------------------------------------------------#
    # Error handlers
    # ---------------------------------------------------#
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
