from datetime import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings
from yashoes.models import User
# from rest_framework_jwt.utils import jwt_payload_handler
def jwt_payload_handler(user):
    return {
        'user_id': user.pk,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'orig_iat': timegm(
            datetime.utcnow().utctimetuple()
        ),
        'aud': api_settings.JWT_AUDIENCE,
        'iss': api_settings.JWT_ISSUER
    }

def jwt_get_username_from_payload_handler(payload):
    id = payload.get('user_id')
    return User.objects.get(id=id).username
