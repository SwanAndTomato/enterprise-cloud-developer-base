#!/bin/bash
#create lambda function
echo "Installing dependencies for coupons_import"
npm install --prefix ./lambda/coupons_import
[ $? == 0 ] || fail 1 "Failed to install dependencies"

echo "Creating deployment package for coupons_import function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_import
zip -r "${PROJECT_DIR}/coupons_import.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

echo "Creating coupons_import function"
awslocal lambda create-function \
    --function-name "coupons_import" \
    --runtime "nodejs18.x" \
    --zip-file fileb://coupons_import.zip \
    --handler "index.handler" \
    --role "arn:aws:iam::000000000000:role/coupons_production_role" \
    --memory-size 128
[ $? == 0 ] || fail 3 "Failed to create function"
echo "coupons_import function created successfully"

#update lambda function
awslocal lambda update-function-code --function-name coupons_import --zip-file fileb://coupons_import.zip
echo "Lambda function 'coupons_import' updated with new code."

# Create resources, methods, and integrate with Lambda function
awslocal apigateway create-rest-api --name coupons-api

