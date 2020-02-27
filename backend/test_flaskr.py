import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

casting_assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgyNzkwMTIwLCJleHAiOjE1ODI3OTczMjAsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.UqmGRRe2uvqpnlvA1-fKScDq2aKrA8yyP_E_pL7i-b1GmPKxG9Uij18msH4PT_Nhi0qhGOyUN4mV26mtr4DSm1z3sEZOPJZ5rAUVfb36IeoGfHxJoFKxvnRNIX5xHJH16F0J0MMAD4xIiC1PdFgYaIKQdO9NO6VYZ5-5z_q6R3SMZb6tsUZHu3uNS_KDdF_RV6FjlWz0IxjMy-2QvG3DAkZp7K8sgup9y5Qo6gwG93xBkL8oy_M5kqWJsfp-NWa47W9-fk5Uuc1iyUBPZvjd43GZyDxh-181Bw7R3oOBXSYcG64PDRmHMjiXayRKyAA1e9uC6uJxemVoeD-1JzMKjw'
# casting_director_token = "Bearer {}".format(os.environ.get('DIRECTOR_JWT'))
exec_producer_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgyNzk1NDE0LCJleHAiOjE1ODI4MDI2MTQsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Rzg14PU2wxYhGDu4yoevQaakASKZc8H2BWIdWOwzyu5KJNC1GgkkW7jY2_TEG0AgD-9M5POJftZQ6FTNluO39JNN2ZqC3UZBy2YFwe68WjT2Dv5G513WnE8emLN5TUqEaYAqtJhsXhjckbJronGJx4wtiE9mPMoFyfuAEwYH29v3GYpeAGrsWaLDcpWT96IwdTICc1PtmISYGQTLqzzV7XugCLDuZbG-lFCGKxxu7zfhZ6kGDNWf6Mg8ck0oyW1z1CdOXX_3xUEuqRTwDMIoGRzpcFCH7gUR0dHRI4IRSmXOUYvNB82StNdJCjZKQVFHOWoKxVDfp4QPJ81gbfA2ag'
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
        res = self.client().get('/')
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

    def test_delete_a_movie(self):
        res = self.client().delete('/movies/4', headers={ "Authorization":(exec_producer_token)})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(movie, None)
        self.assertEqual(data['success'], True)
        self.assertEqual(int(data['deleted_movie'['id']]), 4)
    


    #----------------------------------------------------------#
    # Tests for error behavior of each endpoint
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    # Tests of RBAC for each role
    #----------------------------------------------------------#


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()