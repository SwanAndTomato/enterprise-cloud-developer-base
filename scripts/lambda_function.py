import json

def lambda_handler(event, context):
    # Sample response in the format of t1_sample_coupons_list_response.json
    return {
        'statusCode': 200,
        'body': json.dumps({
            'coupons': [
                {'id': 1, 'name': '50% Off', 'description': 'Get 50% off your next purchase.'},
                {'id': 2, 'name': '10% Off', 'description': 'Get 10% off on select items.'}
            ]
        })
    }
