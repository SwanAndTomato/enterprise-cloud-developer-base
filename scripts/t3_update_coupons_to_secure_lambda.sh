#!/bin/bash

#installing dependencies
echo "Installing dependencies for coupons_to_secure"
npm install --prefix ./lambda/coupons_to_secure
[ $? == 0 ] || fail 1 "Failed to install dependencies"

#creating deployment package
echo "Creating deployment package for coupons_to_secure function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_to_secure
zip -r "${PROJECT_DIR}/coupons_to_secure.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

# create Lambda function
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

#update Lambda function
awslocal lambda update-function-code \
    --function-name coupons_to_secure \
    --zip-file fileb://coupons_to_secure.zip
