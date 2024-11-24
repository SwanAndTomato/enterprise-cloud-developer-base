import json
from unittest.mock import patch
from .. import lambda_function_update

@patch('lambda_function_update.table.update_item')
def test_lambda_handler(mock_update_item):
    event = {
        'pathParameters': {'id': '123'},
        'body': json.dumps({
            'name': 'Updated Coupon',
            'description': 'Updated Description',
            'discount': '30%'
        })
    }

    response = lambda_function_update.lambda_handler(event, None)

    # Assert that the status code is 200
    assert response['statusCode'] == 200
    assert json.loads(response['body'])['message'] == 'Coupon updated successfully'
