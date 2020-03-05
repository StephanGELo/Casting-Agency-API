import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

# casting_assistant_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJEN3VjWmdVUW9Cd3Q2RjBNWGdGbVFpekxBNDJyMVk1WEBjbGllbnRzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU4MzI2OTQ2NSwiZXhwIjoxNTgzMzU1ODY1LCJhenAiOiJEN3VjWmdVUW9Cd3Q2RjBNWGdGbVFpekxBNDJyMVk1WCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.UGfytvS_UkN-k8j11xFxJaKnSxo0VxBPFAvxSgqgCy3AIY7y-fruvt6qmTAE2JZEMJYbK_c7LcC9XdnpJQSod8Tt6pDs00XB2z0uOJ9oaBkfzyC1H7YjtqbsFqFg0-jZ7kWj3l6yOPaVfrtMHc9hWJcMnxael2miqp1L5aEnvD3Kv9-1fij6JYR6yjdNEvYPpUE3-M_tVHxF-QX1RdNrTNmZ1vBK3PytwEwa36wztHvNPHYy1pdVxZEbNPtJYfgbqb4lZQuqmqPJtgJ0nH9cGrKJgSw2kgRSBLGiBk53U1mHmt9ytQr1iyuKPUA5kKl0mRDh1ADgXpYjihQ88-cnhg"
# casting_director_token = "Bearer {}".format(os.environ.get('DIRECTOR_JWT'))
producer = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgzMzY2NzEwLCJleHAiOjE1ODM0MDI3MTAsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.QOGZOH-zYAci4ot0w-Z0-p6ZsY_URou2NN4Vc-HEO6ebJIvgGN1UKnNQh2-Ly2oL3KRShAsnwwRVD-F8_IHNFQDiLk0WGXq6J9V8J8M-UNcs4iLtJOl0RUe2qnKp4akmIqer5ABXORn26TUZSD3UqJYTQpa5rzbAaHXj9mwI5s95lsrkWMBoYTZgctxKatzLK4BIgEmEweJg_nd9E7-1_6cb4GkBWezGzgsBQIb4DS7H4Z2TwA5TYSWZ678JvPyM1u1pAla4xM2oPfqgLJgxMx7p8zfoglhjBbit0iCNTkl7cJ8K2Q_TvG24waHRoYLJJw81zK6MAIjwm-vh7XBI9Q"
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
        self.database_path = 'postgresql://{}/{}'.format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'A new movie',
            'release_date': 'March 3rd'
        }

        self.new_actor = {
            'name': "Russell Poke",
            'age': 27,
            'gender': 'Male',
            'movie': 2
        }

        self.patch_movie = {
            'title' : "L'homme qui pleure",
            'release_date': 'March 30, 2020'
        }

        # Binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        ''' Executed after each test'''
        pass

    #----------------------------------------------------------#
    # Tests for success behavior of each endpoint
    #----------------------------------------------------------#
    #------------------------------#
    # Movies Endpoints
    #------------------------------#
    def test_get_movies_index(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) > 0)

    def test_get_movies(self):
        res = self.client().get('/movies-details', headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) > 0)
    
    def test_add_a_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added_movie'])
        self.assertTrue(len(data['added_movie']) == 1)

    def test_delete_a_movie(self):
        res = self.client().delete('/movies/3', headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(movie, None)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_movie'])

    def test_modify_a_movie(self):
        res = self.client().patch('/movies/4', json=self.patch_movie, headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['updated_movie']) == 1)

    #------------------------------#
    # Actors Endpoints
    #------------------------------#
    def test_get_actors_index(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']) > 0)
    
    def test_get_actors_details(self):
        res = self.client().get('/actors-details', headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']) > 0)
    
    def test_add_an_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added_actor'])
        self.assertTrue(len(data['added_actor']) == 1)
    
    def test_delete_an_actor(self):
        res = self.client().delete('/actors/1', headers={ "Authorization":(producer)})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(movie, None)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_actor'])

    
    
    #----------------------------------------------------------#
    # Tests for error behavior of each endpoint
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    # Tests of RBAC for each role
    #----------------------------------------------------------#


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()