#!/bin/bash

# Create an API Gateway REST API
api_id=$(aws --endpoint-url=http://localhost:4566 apigateway create-rest-api --name "coupons_poc_api" --query 'id' --output text)

# Get the root resource ID
root_id=$(aws --endpoint-url=http://localhost:4566 apigateway get-resources --rest-api-id $api_id --query 'items[0].id' --output text)

# Create a resource for /coupons_poc
resource_id=$(aws --endpoint-url=http://localhost:4566 apigateway create-resource --rest-api-id $api_id --parent-id $root_id --path-part "coupons_poc" --query 'id' --output text)

# Set up a GET method for the /coupons_poc resource
aws --endpoint-url=http://localhost:4566 apigateway put-method \
    --rest-api-id $api_id \
    --resource-id $resource_id \
    --http-method GET \
    --authorization-type "NONE"

# Link the GET method to the Lambda function
aws --endpoint-url=http://localhost:4566 apigateway put-integration \
    --rest-api-id $api_id \
    --resource-id $resource_id \
    --http-method GET \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:coupons_list/invocations"

# Deploy the API
aws --endpoint-url=http://localhost:4566 apigateway create-deployment --rest-api-id $api_id --stage-name "prod"
