import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

# ------------------------#
# Movie model
# ------------------------#

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500))
    created = db.Column(db.DateTime, server_default=db.func.now())
    actors = db.relationship('Actor', backref='movies', lazy=True)

    def __repr__(self):
        return f'<Movie %r>' % self

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # def short(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'release_date': self.release_date,
    #         'image_link': self.image_link,
    #         'created_on': self.created.isoformat()
    #     }

    # def detailed(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'release_date': self.release_date,
    #         'image_link':self.image_link,
    #         'created_on':self.created.isoformat(),
    #         'actors': self.actors
    #     }

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'image_link':self.image_link,
            'created_on':self.created,
            'actors': self.actors
        }


# ------------------------#
# Actor model
# ------------------------#

class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    image_link = db.Column(db.String(500))
    created = db.Column(db.DateTime, server_default=db.func.now())
    movie = db.Column(db.Integer, db.ForeignKey('movies.id'))


    def __repr__(self):
        return f'<Actor %r>' % self

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_name(self):
       return self.name

    # def short(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'age': self.age,
    #         'gender': self.gender,
    #         'image_link': self.image_link,
    #         'added_on': self.created
    #     }

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'image_link': self.image_link,
            'added_on':self.created,
            'movie': self.movie
        }
