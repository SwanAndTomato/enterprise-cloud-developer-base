import boto3
import json

s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
bucket_name = "coupons"

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        filename = body.get('filename')

        if not filename:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Filename is required"})
            }

        # Generate a presigned URL
        url = s3.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key': filename}, ExpiresIn=3600)

        return {
            "statusCode": 200,
            "body": json.dumps({"url": url})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
