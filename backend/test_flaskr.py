import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


producer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgzMzY2NzEwLCJleHAiOjE1ODM0MDI3MTAsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.QOGZOH-zYAci4ot0w-Z0-p6ZsY_URou2NN4Vc-HEO6ebJIvgGN1UKnNQh2-Ly2oL3KRShAsnwwRVD-F8_IHNFQDiLk0WGXq6J9V8J8M-UNcs4iLtJOl0RUe2qnKp4akmIqer5ABXORn26TUZSD3UqJYTQpa5rzbAaHXj9mwI5s95lsrkWMBoYTZgctxKatzLK4BIgEmEweJg_nd9E7-1_6cb4GkBWezGzgsBQIb4DS7H4Z2TwA5TYSWZ678JvPyM1u1pAla4xM2oPfqgLJgxMx7p8zfoglhjBbit0iCNTkl7cJ8K2Q_TvG24waHRoYLJJw81zK6MAIjwm-vh7XBI9Q"
director_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTFiNWYzZjQ2NTk1OTBjYzc4NjZmM2IiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgzMzk2Njk1LCJleHAiOjE1ODM0MzI2OTUsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbHMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.KMBDc0zOzd9FrY9cfvOd3SGLUrd6s39Jst6S9bVly_Q_lppqUG-9N0lc-IMWhA5Sbv_ro3iOc6eVG5fMmMuBrAHplUrnClbrYfOf1xn9enlJGcJWWLEdIEYRdVgixW8F0ikLFUGwcq0HULxL2lHB61tvIeKPl7l8hPViPkMF10Cgj_Xr0Q4QUe6QVCKO8AagETWqJg5PKT8rnlJ-GJ9_tv7Sc1Iv-v8RvZxomvyDmPgmzZpiKo2itqB2hU2cVh_Hpcinqx4bjgJjuR_Mx0HbY90zbUS8RjCgYaE_CIWf7SWIVIcxmJDC-ghMvTEJWv-YZlgS9eNr5UVgM8uwB4WWwA'
assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTFiNjZjZjBjZmU3MzBjYzFiNGU5OTgiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgzMzk2OTIzLCJleHAiOjE1ODM0MzI5MjMsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlscyJdfQ.MWiiU6gR6bTDHRzYMKjZgaZmriFPBY3tTquPGeHRnEq8BO9_zFdvtz5LUMLn4Fr1mxJSRMr_9S7xJR80Zr11UNuB3WMqQ7stEyDBF4QBKGf_SWDzCe4LNM_-kv2x5Z2d7W2-emN8BvIG01H-8dirNlWblXYfT529UJRDMQyiVvNoj3F7mGplcEnleIS_tlqofTTBfXh1iDClQJA0zphH0R5OkxV5WEbpwxAmvBLnfM9ftUZ8de6O9-imzItLpGL4E17ZA-xWfy1pyujZ2HFH2_CZE7QPkWrs5DCbNq8KC7ecO0WoI5T40p6Xe2hYRlk5gVoa-WOSaNIG8UqL1IOEww'
unregistered_user = 'Bearer IWantToGetdata'

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
            'name': 'Russell Poke',
            'age': 27,
            'gender': 'Male',
            'movie': 2
        }

        self.patch_movie = {
            'title' : "L'homme qui pleure",
            'release_date': 'March 30, 2020'
        }

        self.patch_actor = {
            'name': 'Lisette Riseborough',
            'age': 30,
            'gender': 'Female',
            'movie': 2
        }

        self.bad_movie_request = {
            'title': "1840",
            'release_date': ""
        }

        self.bad_actor_request = {
            'name': 'Charlie Chaplin',
            'age': '',
            'gender':'Male',
            'movie': 2
        }

        self.wrong_patch_movie = {
            'title' : "",
            'release_date': 'March 30, 2020'
        }

        self.wrong_patch_actor = {
            'name': 'Richard Brandson',
            'age': 65,
            'gender': '',
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
        res = self.client().get('/movies-details', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) > 0)

    def test_delete_a_movie(self):
        res = self.client().delete('/movies/4', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(movie, None)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_movie'])
    
    def test_add_a_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added_movie'])
        self.assertTrue(len(data['added_movie']) == 1)

    def test_modify_a_movie(self):
        res = self.client().patch('/movies/3', json=self.patch_movie, headers={ "Authorization":(producer_token)})
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
        res = self.client().get('/actors-details', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']) > 0)
    
    def test_add_an_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added_actor'])
        self.assertTrue(len(data['added_actor']) == 1)
    
    def test_delete_an_actor(self):
        res = self.client().delete('/actors/4', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(actor, None)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_actor'])

    def test_modify_an_actor(self):
        res = self.client().patch('/actors/3', json=self.patch_actor, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['updated_actor']) == 1)

    
    #----------------------------------------------------------#
    # Tests for error behavior of each endpoint
    #----------------------------------------------------------#
    #----------------------------------#
    # Movies Endpoints - error behavior
    #----------------------------------#
    def test_404_get_movies_beyond_valid_page(self):
        res = self.client().get('/movies?page=500')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_401_get_movies_details_not_authorized(self):
        res = self.client().get('/movies-details', headers={ "Authorization":(unregistered_user)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')

    def test_400_add_a_movie_incorrectly(self):
        res = self.client().post('/movies', json=self.bad_movie_request, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_404_not_found_if_deleting_a_movie_with_non_existant_id(self):
        res = self.client().delete('/movies/1000', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_422_unprocessed_if_updating_a_movie_with_insufficient_data(self):
        res = self.client().patch('/movies/2', json=self.wrong_patch_movie, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    #----------------------------------#
    # Actors Endpoints - error behavior
    #----------------------------------#
    def test_404_get_actors_beyond_valid_page(self):
        res = self.client().get('/actors?page=500')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')
    
    def test_401_get_actors_details_not_authorized(self):
        res = self.client().get('/actors-details', headers={ "Authorization":(unregistered_user)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')

    def test_400_add_an_actor_incorrectly(self):
        res = self.client().post('/actors', json=self.bad_actor_request, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')

    def test_404_not_found_if_deleting_an_actor_with_non_existant_id(self):
        res = self.client().delete('/actors/1000', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_422_unprocessed_if_updating_an_actor_with_insufficient_data(self):
        res = self.client().patch('/actors/2', json=self.wrong_patch_actor, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    #----------------------------------------------------------#
    # Two Tests of RBAC for each role
    #----------------------------------------------------------#
    #----------------------------------#
    # Executive Producer
    #----------------------------------#
    def test_producer_get_movies(self):
        res = self.client().get('/movies-details', headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) > 0)

    def test_producer_modify_a_movie(self):
        res = self.client().patch('/movies/2', json=self.patch_movie, headers={ "Authorization":(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['updated_movie']) == 1)

    #----------------------------------#
    # Casting Director
    #----------------------------------#
    def test_director_delete_an_actor(self):
        res = self.client().delete('/actors/2', headers={ "Authorization":(director_token)})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(actor, None)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_actor'])

    def test_director_modify_an_actor(self):
        res = self.client().patch('/actors/5', json=self.patch_actor, headers={ "Authorization":(director_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['updated_actor']) == 1)

    #----------------------------------#
    # Casting Assistant
    #----------------------------------#
    def test_assistant_get_movies(self):
        res = self.client().get('/movies-details', headers={ "Authorization":(assistant_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) > 0)

    def test_assistant_unauthorized_to_modify_an_actor(self):
        res = self.client().patch('/actors/4', json=self.patch_actor, headers={ "Authorization":(assistant_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()