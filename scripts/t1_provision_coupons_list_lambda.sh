#!/bin/bash

# Get the role ARN for coupons_lambda_role
role_arn=$(aws --endpoint-url=http://localhost:4566 iam get-role --role-name coupons_lambda_role --query 'Role.Arn' --output text)

# Check if the role ARN was retrieved
if [ -z "$role_arn" ]; then
    echo "Failed to retrieve IAM Role ARN for coupons_lambda_role"
    exit 1
fi

# Create the Lambda function
aws --endpoint-url=http://localhost:4566 lambda create-function \
    --function-name coupons_list \
    --runtime python3.8 \
    --role $role_arn \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://coupons_list_lambda.zip
