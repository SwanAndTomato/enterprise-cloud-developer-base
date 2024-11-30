import json
import boto3
import bcrypt
import jwt
from datetime import datetime, timedelta

# Constants
SECRET = "0HXc4w5NEzA61HkV"
DYNAMODB_TABLE = "users"

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        username = body.get("username")
        password = body.get("password")

        if not username or not password:
            return {
                "statusCode": 403,
                "body": json.dumps({"message": "Invalid credentials"})
            }

        # Retrieve user data from DynamoDB
        dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566")
        table = dynamodb.Table(DYNAMODB_TABLE)
        response = table.get_item(Key={"username": username})
        user = response.get("Item")

        if not user or not bcrypt.checkpw(password.encode(), user["password"].encode()):
            return {
                "statusCode": 403,
                "body": json.dumps({"message": "Invalid credentials"})
            }

        # Generate JWT token
        expiration_time = datetime.now(datetime.timezone.utc) + timedelta(hours=1)
        token = jwt.encode(
            {"username": username, "exp": expiration_time},
            SECRET,
            algorithm="HS256"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "token": token,
                "expiresAt": expiration_time.isoformat() + "Z"
            })
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
