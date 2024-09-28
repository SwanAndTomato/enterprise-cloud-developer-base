#!/bin/bash

# Get the role ARN for coupons_lambda_role
role_arn=$(aws --endpoint-url=http://localhost:4566 iam get-role --role-name coupons_lambda_role --query 'Role.Arn' --output text)

# Update the Lambda function to update coupon by id
aws --endpoint-url=http://localhost:4566 lambda update-function-code \
    --function-name coupons_update \
    --zip-file fileb://coupons_update_lambda.zip