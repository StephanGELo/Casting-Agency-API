import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

casting_assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgzMjIwNTg5LCJleHAiOjE1ODMyMjc3ODksImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.B-r82EAKENq7QSrQU7gROo0sL2pzQDboATmc6_wyGh425BWHptY1auldzIn6Z59nZC8ozDMx63bilQk9aH3oaqy6Xs5t06yXRUAU_COxTDvmVTQuxjbJeJEHK5IM1cQUmg3ap6GNeTx6GstgZ55coXFAtKJhtjolra6lou1WrvNAYuzRqvA1tOWAlY9EdwAn9vZcey4dSMz9iniNpHU7lv8T0--nwsJsEo1rUihFTQ6au2KHbPhDnsSe7iehwzSmUO0vhUe0myNZuYJLZeS4OJLKggah1rp7frprKPN19nqxTvTM72S3a-pUnrxw0RzhU4kgn-ZAAdq0hcnnoZgjFQ'
# casting_director_token = "Bearer {}".format(os.environ.get('DIRECTOR_JWT'))
exec_producer_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgzMjIwNTg5LCJleHAiOjE1ODMyMjc3ODksImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.B-r82EAKENq7QSrQU7gROo0sL2pzQDboATmc6_wyGh425BWHptY1auldzIn6Z59nZC8ozDMx63bilQk9aH3oaqy6Xs5t06yXRUAU_COxTDvmVTQuxjbJeJEHK5IM1cQUmg3ap6GNeTx6GstgZ55coXFAtKJhtjolra6lou1WrvNAYuzRqvA1tOWAlY9EdwAn9vZcey4dSMz9iniNpHU7lv8T0--nwsJsEo1rUihFTQ6au2KHbPhDnsSe7iehwzSmUO0vhUe0myNZuYJLZeS4OJLKggah1rp7frprKPN19nqxTvTM72S3a-pUnrxw0RzhU4kgn-ZAAdq0hcnnoZgjFQ'
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
            'title': 'A new movie',
            'release_date': 'March 3rd'
        }

        self.new_actor = {
            'name': "Russell Poke",
            'age': 27,
            'gender': 'Male',
            'movie_id': 2
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
        res = self.client().get('/movies-details', headers={ "Authorization":(casting_assistant_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) > 0)
    
    # def test_add_a_movie(self):
    #     res = self.client().post('/movies', json=self.new_movie, headers={ "Authorization":(exec_producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['added_movie'])
    #     self.assertTrue(len(data['added_movie']) == 1)

    # def test_delete_a_movie(self):
    #     res = self.client().delete('/movies/4', headers={ "Authorization":(exec_producer_token)})
    #     data = json.loads(res.data)

    #     movie = Movie.query.filter(Movie.id == 4).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(movie, None)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['deleted_movie'])
    
    # def test_modify_a_movie(self):
    #     res = self.client().patch('/movies/3', json=self.patch_movie, headers={"Authorization": (exec_producer_token)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['movie']) == 1)
    
    #----------------------------------------------------------#
    # Tests for error behavior of each endpoint
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    # Tests of RBAC for each role
    #----------------------------------------------------------#


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()