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
        movies = Movie.query.all()
        formatted_movies = [movie.short() for movie in movies]
        selected_movies = paginate_items(request, formatted_movies)

        try:
            return jsonify({
                "success": True,
                "movies": selected_movies
            })
        except Exception:
            abort(422)


    #---------------------------------------------------#
    # Movies
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
        
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth("delete:movies")
    def delete_a_movie(token, id):
        print("id is >>>", id)
        movie = Movie.query.get(id)
        try:
            movie.delete()

            return jsonify({
                "success": True,
                "deleted_movie": movie.format()
            })
        except Exception:
            abort(404)

    @app.route('/movies', methods=['POST'])
    @requires_auth("post:movies")
    def add_a_movie(token):
        body = request.get_json()
        print(body)
        new_title = body.get('title', None)
        print(new_title)
        new_release_date = body.get('release_date', None)

        try:
            new_movie = Movie(
                title=new_title,
                release_date=new_release_date
            )

            new_movie.insert()
            movie = Movie.query.get(new_movie.id).short()    

            return jsonify({
                "success": True,
                "added_movie": [movie]
            })
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
    # Actors
    #---------------------------------------------------#
    @app.route('/actors', methods=['GET'])
    @requires_auth("get:actors")
    def get_actors(token):
        actors = Actor.query.all()
        paginated_actors = paginate_items(request, actors)
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
        print("hello THERE", body)

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        try:
            new_actor = Actor(
                name=new_name,
                age=new_age,
                gender=new_gender
            )

            new_actor.insert()
            actor = Actor.query.get(new_actor.id).format()    

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

        actor.name = new_name
        actor.age = new_age
        actor.gender = new_gender
        actor.update()
        updated_actor = [Actor.query.get(id).format()]

        return jsonify({
            "success": True,
            "updated_actor":[updated_actor]
        })
    
    return app      