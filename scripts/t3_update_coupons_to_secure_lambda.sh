#!/bin/bash

echo "Installing dependencies for coupons_to_secure"
npm install --prefix ./lambda/coupons_to_secure
[ $? == 0 ] || fail 1 "Failed to install dependencies"

echo "Creating deployment package for coupons_to_secure function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_to_secure
zip -r "${PROJECT_DIR}/coupons_to_secure.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

echo "Creating coupons_to_secure function"
awslocal lambda create-function \
    --function-name "coupons_to_secure" \
    --runtime "nodejs18.x" \
    --zip-file fileb://coupons_to_secure.zip \
    --handler "index.handler" \
    --role "arn:aws:iam::000000000000:role/coupons_production_role" \
    --memory-size 128
[ $? == 0 ] || fail 3 "Failed to create function"
echo "coupons_to_secure function created successfully"

awslocal --endpoint-url=http://localhost:4566 lambda update-function-code \
    --function-name coupons_to_secure \
    --zip-file fileb://coupons_to_secure.zip

echo "coupons_to_secure function updated successfully"
