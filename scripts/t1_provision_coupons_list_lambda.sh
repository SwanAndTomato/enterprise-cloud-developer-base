#!/bin/bash

# Get the role ARN for coupons_lambda_role
role_arn=$(aws --endpoint-url=http://localhost:4566 iam get-role --role-name coupons_lambda_role --query 'Role.Arn' --output text)

# Check if the role ARN was retrieved
if [ -z "$role_arn" ]; then
    echo "Failed to retrieve IAM Role ARN for coupons_lambda_role"
    exit 1
fi

# Create the Lambda list function
echo "Creating lambda functions"
echo "Installing dependencies for coupons_list Lambda function"
npm install --prefix ./lambda/coupons_list
[ $? == 0 ] || fail 1 "Failed to install dependencies"

# Create the Lambda function package
echo "Creating deployment package for coupons_list Lambda function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_list
zip -r "${PROJECT_DIR}/coupons_list.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

# Create the Lambda function
awslocal lambda create-function \
    --function-name "coupons_list" \
    --runtime "nodejs18.x" \
    --zip-file fileb://coupons_list.zip \
    --handler "index.handler" \
    --role "arn:aws:iam::000000000000:role/coupons_production_role" \
    --memory-size 128
[ $? == 0 ] || fail 3 "Failed to create Lambda function"


