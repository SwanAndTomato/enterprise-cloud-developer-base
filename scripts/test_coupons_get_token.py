import pytest
import json
import bcrypt
from moto import mock_aws
import boto3
from coupons_get_token import handler

# Constants
DYNAMODB_TABLE = "users"

@pytest.fixture
def setup_dynamodb():
    with mock_aws():
        # Create mock DynamoDB table
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.create_table(
            TableName=DYNAMODB_TABLE,
            KeySchema=[{"AttributeName": "username", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "username", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST"
        )
        table.put_item(
            Item={
                "username": "tester1",
                "password": bcrypt.hashpw("Pc4RM0AMKy5aSGfD".encode(), bcrypt.gensalt(12)).decode()
            }
        )
        yield table


def test_valid_credentials(setup_dynamodb):
    event = {
        "body": json.dumps({
            "username": "tester1",
            "password": "Pc4RM0AMKy5aSGfD"
        })
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert "token" in body
    assert "expiresAt" in body


def test_invalid_credentials(setup_dynamodb):
    event = {
        "body": json.dumps({
            "username": "tester1",
            "password": "wrongPassword"
        })
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 403
    assert body["message"] == "Invalid credentials"


def test_nonexistent_user(setup_dynamodb):
    event = {
        "body": json.dumps({
            "username": "nonexistent",
            "password": "Pc4RM0AMKy5aSGfD"
        })
    }

    response = handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 403
    assert body["message"] == "Invalid credentials"
