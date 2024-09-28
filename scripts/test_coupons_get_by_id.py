import json
from unittest.mock import patch
import lambda_function_get_by_id

@patch('lambda_function_get_by_id.table.get_item')
def test_lambda_handler(mock_get_item):
    # Mock the DynamoDB response
    mock_get_item.return_value = {
        'Item': {
            'id': '123',
            'name': 'Test Coupon',
            'description': 'Test Description',
            'discount': '50%'
        }
    }

    event = {
        'pathParameters': {'id': '123'}
    }

    response = lambda_function_get_by_id.lambda_handler(event, None)
    
    # Assert that the status code is 200 and the item was returned correctly
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['id'] == '123'
    assert body['name'] == 'Test Coupon'
    assert body['description'] == 'Test Description'
    assert body['discount'] == '50%'
