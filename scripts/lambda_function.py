import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
table = dynamodb.Table('coupons')

def lambda_handler(event, context):
    # Extract the coupon ID from the path parameters
    coupon_id = event['pathParameters']['id']

    # Extract the updated data from the request body
    body = json.loads(event['body'])

    # Update the item in the DynamoDB table
    try:
        table.update_item(
            Key={'id': coupon_id},
            UpdateExpression="set #name=:n, #desc=:d, #discount=:dc",
            ExpressionAttributeNames={
                '#name': 'name',
                '#desc': 'description',
                '#discount': 'discount'
            },
            ExpressionAttributeValues={
                ':n': body['name'],
                ':d': body['description'],
                ':dc': body['discount']
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Coupon updated successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
