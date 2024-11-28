import pytest
import json
import jwt
from datetime import datetime, timedelta
from coupons_to_secure import handler

# Constants
SECRET = "0HXc4w5NEzA61HkV"

def generate_token(username, expired=False):
    expiration_time = datetime.utcnow() + (timedelta(hours=-1) if expired else timedelta(hours=1))
    return jwt.encode(
        {"username": username, "exp": expiration_time},
        SECRET,
        algorithm="HS256"
    )


def test_valid_token():
    valid_token = generate_token("tester1")
    event = {
        "headers": {
            "Authorization": f"Bearer {valid_token}"
        }
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert body["message"] == "Token is valid"


def test_expired_token():
    expired_token = generate_token("tester1", expired=True)
    event = {
        "headers": {
            "Authorization": f"Bearer {expired_token}"
        }
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 403
    assert body["message"] == "Token has expired"


def test_invalid_token():
    event = {
        "headers": {
            "Authorization": "Bearer invalidToken"
        }
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 403
    assert body["message"] == "Invalid token"


def test_missing_token():
    event = {
        "headers": {}
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 403
    assert body["message"] == "Invalid token"
