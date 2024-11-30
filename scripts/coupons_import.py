import json
import boto3

s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
bucket_name = "coupons"

def lambda_handler(event, context):
    try:
        # Extract details from the event
        body = json.loads(event['body'])
        coupon_id = body.get('coupon_id')
        data = body.get('data')

        if not coupon_id or not data:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing coupon_id or data"})
            }

        # File name and upload
        file_name = f"{coupon_id}.json"
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Success", "file": file_name})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
