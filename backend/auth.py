import json
from flask import Flask, request, request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urlib.request import urlopen

AUTH0_DOMAIN = 'universaleagle.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'castingagency'


#----------------------------------------------------------#
# AuthError Exception
#----------------------------------------------------------#
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


#----------------------------------------------------------#
# Auth Header
#----------------------------------------------------------#

def get_token_auth_header():
    authorization_header = request.headers.get('Authorization', None)
    if not authorization_header:
        raise AuthError({
            'code': 'missing_header',
            'description': 'The header must contain a "Bearer".'
        }, 401)
    
    elif len(header_parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'The header must contain a bearer and the token.'
        }, 401)

    token = header_parts[1]
    return token
