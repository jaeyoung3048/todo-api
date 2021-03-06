import jwt
from utils.secrets import *


def encode_jwt(data):
    return jwt.encode(data, get_secret("SECRET_KEY"), algorithm="HS256").decode("utf-8")


def decode_jwt(token):
    return jwt.decode(
        token,
        get_secret("SECRET_KEY"),
        algorithm="HS256",
        options={"verify_aud": False},
    )
