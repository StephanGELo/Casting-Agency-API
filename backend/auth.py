import json
from flask import Flask, request, request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urlib.request import urlopen

AUTH0_DOMAIN = 'universaleagle.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'castingagency'

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code