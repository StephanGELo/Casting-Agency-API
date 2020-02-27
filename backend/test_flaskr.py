import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from .app import create_app
from .models import setup_db, Movie, Actor

#----------------------------------------------------------#
# Unittest Test Cases
#----------------------------------------------------------#
class CastingAgencyTestCase(unittest.TestCase):
    '''
    This class represents the casting agency test case
    '''

    def setUp(self):
        '''
        Define test variables and initialize app
        '''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'castingagency_test'
        self.database_path = 'postgres://{}/{}'.format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': '',
            'release_date': 'March 3rd'
        }

        self.new_actor = {
            'name': "Russell Poke",
            'age': 27,
            'gender': 'Male',
            'movie_id': 2
        }

        # Binds the app to the current context
        with self.app.app_context():
            self.db = SQLAchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        ''' Executed after each test'''
        pass

    #----------------------------------------------------------#
    # Tests for success behavior of each endpoint
    #----------------------------------------------------------#
    def test_get_movies_index(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies(self):
        res = self.client().get('/movies-details')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    


    #----------------------------------------------------------#
    # Tests for error behavior of each endpoint
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    # Tests of RBAC for each role
    #----------------------------------------------------------#


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()