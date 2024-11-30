import boto3
import json

def lambda_handler(event, context):
    sns_client = boto3.client('sns', endpoint_url='http://localhost:4566')  # LocalStack endpoint
    
    try:
        # Extract message from the event (adjust the key based on the event structure)
        message = event.get("message", "Default notification message")
        
        # Parameters for SNS
        response = sns_client.publish(
            TopicArn='arn:aws:sns:us-east-1:000000000000:coupons',
            Message=message
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Notification sent successfully",
                "response": response
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error sending notification",
                "error": str(e)
            })
        }
