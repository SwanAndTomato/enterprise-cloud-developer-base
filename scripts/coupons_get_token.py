import json
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
import boto3

# Constants for JWT
SECRET_KEY = '0HXc4w5NEzA61HkV'  # Use the provided secret
JWT_EXP_DELTA_SECONDS = 3600  # Token expiration time (e.g., 1 hour)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
users_table = dynamodb.Table('users')

def lambda_handler(event, context):
    # Parse the request body for username and password
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']
    
    # Query DynamoDB for the user
    response = users_table.get_item(Key={'username': username})
    user = response.get('Item')
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        # Generate JWT if the password matches
        payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # Successful response with token
        return {
            'statusCode': 200,
            'body': json.dumps({
                'token': token,
                'expires_in': JWT_EXP_DELTA_SECONDS
            })
        }
    else:
        # Invalid credentials response
        return {
            'statusCode': 403,
            'body': json.dumps({'message': 'Invalid credentials'})
        }
