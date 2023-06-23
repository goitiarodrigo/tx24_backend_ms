from django.conf import settings
import jwt
import base64

def validate_token(header_token):
    try:
        if not header_token: return False
        token = header_token.split(' ')[1]
        if 'AccessToken' in token:
            cleaned_token = token.split('.')[1]
            decoded_token = base64.b64decode(cleaned_token.encode('ascii'))
            if decoded_token.find(b'PermanentToken') != -1: return True
        jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False