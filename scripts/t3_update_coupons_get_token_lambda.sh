#!/bin/bash
echo "Installing dependencies for coupons_get_token"
npm install --prefix ./lambda/coupons_get_token
[ $? == 0 ] || fail 1 "Failed to install dependencies"

echo "Creating deployment package for coupons_get_token function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_get_token
zip -r "${PROJECT_DIR}/coupons_get_token.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

echo "Creating coupons_get_token function"
awslocal lambda create-function \
    --function-name "coupons_get_token" \
    --runtime "nodejs18.x" \
    --zip-file fileb://coupons_get_token.zip \
    --handler "index.handler" \
    --role "arn:aws:iam::000000000000:role/coupons_production_role" \
    --memory-size 128
[ $? == 0 ] || fail 3 "Failed to create function"
echo "coupons_get_token function created successfully"

#update lambda function
awslocal lambda update-function-code \
    --function-name coupons_get_token \
    --zip-file fileb://coupons_get_token.zip
