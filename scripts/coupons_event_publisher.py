import boto3
import json

def lambda_handler(event, context):
    kinesis_client = boto3.client('kinesis', endpoint_url='http://localhost:4566')  # LocalStack endpoint
    
    try:
        # Serialize the incoming event
        payload = json.dumps(event)
        
        # Parameters for Kinesis
        response = kinesis_client.put_record(
            StreamName='coupons',
            PartitionKey='partitionKey',  # Adjust as needed
            Data=payload
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Message published successfully",
                "response": response
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error publishing message",
                "error": str(e)
            })
        }
