import json
import lambda_function  # Assuming lambda_function.py is in the same directory

def test_lambda_handler():
    # Call the handler function
    result = lambda_function.lambda_handler({}, None)
    
    # Assert that statusCode is 200
    assert result['statusCode'] == 200
    
    # Assert that the body contains the expected JSON structure
    body = json.loads(result['body'])
    assert 'coupons' in body
    assert len(body['coupons']) > 0
