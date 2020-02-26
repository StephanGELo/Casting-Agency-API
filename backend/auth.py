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


#----------------------------------------------------------#
# Check Permissions
#----------------------------------------------------------#
def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permission not included in JWT.'
        }, 400)
    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found.'
        }, 403)

    return True


#----------------------------------------------------------#
# Verify the Token
#----------------------------------------------------------#
def verify_decode_jwt(token):
    # Get the public key from Auth0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # Get the data in the header
    raw_header = jwt.get_unverified_header(token)

    # Choose our key
    rsa_key = {}
    if 'kid' not in raw_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] = raw_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            # Use the key to validate the jwt
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )
            return payload
        
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)
        
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims.\
                    Please, check the audience and issuer.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key'
    }, 401)


#----------------------------------------------------------#
# @requires_auth decorator method
#----------------------------------------------------------#
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            try:
                payload = verify_decode_jwt(token)
            except Exception:
                abort(401)
                check_permissions(permission, payload)
                return f(payload, *args, **kwargs)
        
        return wrapper
    return requires_auth_decorator