import jwt
from django.conf import settings

def validate_token(header_token):
    try:
        if not header_token: return False
        token = header_token.split(' ')[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False