# Type: AWS Lambda Function

import json
import jwt
import os

# JWT Secret Key
SECRET_KEY = '0HXc4w5NEzA61HkV'

def lambda_handler(event, context):
    # Get the Authorization header
    auth_header = event['headers'].get('Authorization')
    
    if auth_header:
        try:
            # Extract the token part (Bearer <token>)
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

            # Successful validation
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Access granted'})
            }
        except jwt.ExpiredSignatureError:
            # Token has expired
            return {'statusCode': 403, 'body': json.dumps({'message': 'Token expired'})}
        except jwt.InvalidTokenError:
            # Token is invalid
            return {'statusCode': 403, 'body': json.dumps({'message': 'Invalid token'})}
    
    # No token provided
    return {'statusCode': 403, 'body': json.dumps({'message': 'Authorization header missing'})}
