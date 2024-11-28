import json
import jwt

# Constants
SECRET = "0HXc4w5NEzA61HkV"

def handler(event, context):
    try:
        # Extract the token from the Authorization header
        headers = event.get("headers", {})
        authorization = headers.get("Authorization")

        if not authorization or not authorization.startswith("Bearer "):
            return {
                "statusCode": 403,
                "body": json.dumps({"message": "Invalid token"})
            }

        token = authorization.split(" ")[1]

        # Validate the token
        try:
            decoded_token = jwt.decode(token, SECRET, algorithms=["HS256"])
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Token is valid"})
            }
        except jwt.ExpiredSignatureError:
            return {
                "statusCode": 403,
                "body": json.dumps({"message": "Token has expired"})
            }
        except jwt.InvalidTokenError:
            return {
                "statusCode": 403,
                "body": json.dumps({"message": "Invalid token"})
            }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
