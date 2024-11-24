import pytest
import json
import os
import requests

# Set the URL for the API Gateway or LocalStack endpoint
API_URL = "http://localhost:4566/restapis/your_api_id/prod/_user_request_/token"

# Function to log results to T3Testing.txt
def log_to_file(message):
    with open("T3Testing.txt", "a") as log_file:
        log_file.write(message + "\n")

# Test case 1: Test valid credentials and token generation
def test_valid_credentials():
    payload = {
        "username": "tester1",
        "password": "Pc4RM0AMKy5aSGfD"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "token" in data, "Token not returned in the response"
    assert "expires_in" in data, "Expiration time not returned in the response"
    
    log_to_file("Test 1 Passed: Valid credentials and token generation.")
    print("Test 1 Passed: Valid credentials and token generation.")

# Test case 2: Test invalid credentials
def test_invalid_credentials():
    payload = {
        "username": "tester1",
        "password": "wrongpassword"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 403, f"Expected 403, got {response.status_code}"
    log_to_file("Test 2 Passed: Invalid credentials returned 403.")
    print("Test 2 Passed: Invalid credentials returned 403.")

# Test case 3: Test valid credentials but check if the token format is correct
def test_token_format():
    payload = {
        "username": "tester1",
        "password": "Pc4RM0AMKy5aSGfD"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    token = data.get("token")
    
    # Token should be a valid JWT format (3 parts separated by dots)
    assert token and len(token.split('.')) == 3, "Token format is invalid"
    
    log_to_file("Test 3 Passed: Token format is valid.")
    print("Test 3 Passed: Token format is valid.")

# Test case 4: Test token expiration field is present
def test_token_expiration():
    payload = {
        "username": "tester1",
        "password": "Pc4RM0AMKy5aSGfD"
    }
    response = requests.post(API_URL, json=payload)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "expires_in" in data, "Expiration time is missing"
    
    log_to_file("Test 4 Passed: Token expiration field is present.")
    print("Test 4 Passed: Token expiration field is present.")

# Run all tests
if __name__ == "__main__":
    pytest.main()
