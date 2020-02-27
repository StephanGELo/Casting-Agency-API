import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

casting_assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgyNzkwMTIwLCJleHAiOjE1ODI3OTczMjAsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.UqmGRRe2uvqpnlvA1-fKScDq2aKrA8yyP_E_pL7i-b1GmPKxG9Uij18msH4PT_Nhi0qhGOyUN4mV26mtr4DSm1z3sEZOPJZ5rAUVfb36IeoGfHxJoFKxvnRNIX5xHJH16F0J0MMAD4xIiC1PdFgYaIKQdO9NO6VYZ5-5z_q6R3SMZb6tsUZHu3uNS_KDdF_RV6FjlWz0IxjMy-2QvG3DAkZp7K8sgup9y5Qo6gwG93xBkL8oy_M5kqWJsfp-NWa47W9-fk5Uuc1iyUBPZvjd43GZyDxh-181Bw7R3oOBXSYcG64PDRmHMjiXayRKyAA1e9uC6uJxemVoeD-1JzMKjw'
# casting_director_token = "Bearer {}".format(os.environ.get('DIRECTOR_JWT'))
exec_producer_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rUTFRVGxHUmtVME5rWXpNekkyT0RjeE56aEVPREEyT1RCR01EVkJSamxEUXpBeVJEVXpRdyJ9.eyJpc3MiOiJodHRwczovL3VuaXZlcnNhbGVhZ2xlLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTA5M2JlMGI5ZWE2YzBjZDFjNTYzZTIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTgyNzkzMDk3LCJleHAiOjE1ODI4MDAyOTcsImF6cCI6IjEweDdtT1R2anVQSWNqMGpGbTVPeTZjZE1rTEFWM0NFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.A0U3ueOo0fb6S2NVZgOL14j6nPjOKtQ4CtlHYXVw9Qr6YJeHD2ym7Bg0ariHm1Ila5uRORtlzw5GiUldJQJA-9Keq7FN523Y5vzfhF7jSfnRvFkXgBALzwmCiip3kvYky800b1s00xrTYHyatqrK4j4Pb4gFrgj5HaexCO3MSS-k7_-a6HvcnQk38c3w6OUb1-w99aVUgwwuHlijJNVCm1dffXigc7rLNXc6HciCd15Bstiiek9JVUK58KiYu_w8zzmNKlV-hzK_5Z7Y_tLX_ie0Lbxtonx_rYyiJluipDHkAVZTQq7oYogdjQhG9jz81isuSBwc7pLw20MmJW5BWQ'
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
    
    def test_add_a_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers={ "Authorization":(exec_producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added_movie'])
        self.assertTrue(len(data['added_movie']) == 1)        

    #----------------------------------------------------------#
    # Tests for error behavior of each endpoint
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    # Tests of RBAC for each role
    #----------------------------------------------------------#


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()