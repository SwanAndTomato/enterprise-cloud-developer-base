#!/bin/bash
set -e  # Exit immediately if any command fails

# Define the fail function for better error handling
fail() {
  echo "ERROR: $2"
  exit $1
}

export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"

echo "Installing dependencies for coupons_get_token"
npm install --prefix ./lambda/coupons_get_token
[ $? == 0 ] || fail 1 "Failed to install dependencies"

echo "Creating deployment package for coupons_get_token function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_get_token

# Clean up old deployment package if exists
rm -f "${PROJECT_DIR}/coupons_get_token.zip"

# Create new deployment package
zip -r "${PROJECT_DIR}/coupons_get_token.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

echo "Creating coupons_get_token function"
awslocal lambda create-function \
    --function-name "coupons_get_token" \
    --runtime "nodejs18.x" \
    --zip-file fileb://coupons_get_token.zip \
    --handler "index.handler" \
    --role "arn:aws:iam::000000000000:role/coupons_lambda_role" \
    --memory-size 128
[ $? == 0 ] || fail 3 "Failed to create function"
echo "coupons_get_token function created successfully"

echo "Updating coupons_get_token function code"
awslocal --endpoint-url=http://localhost:4566 lambda update-function-code \
    --function-name coupons_get_token \
    --zip-file fileb://coupons_get_token.zip

echo "coupons_get_token function updated successfully"
