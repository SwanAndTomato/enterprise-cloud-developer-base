#!/bin/bash

# create lambda function
echo "Installing dependencies for coupons_import_presigned_url"
npm install --prefix ./lambda/coupons_import_presigned_url
[ $? == 0 ] || fail 1 "Failed to install dependencies"

echo "Creating deployment package for coupons_import_presigned_url function"
PROJECT_DIR=$(pwd)
cd ./lambda/coupons_import_presigned_url
zip -r "${PROJECT_DIR}/coupons_import_presigned_url.zip" .
cd $PROJECT_DIR
[ $? == 0 ] || fail 2 "Failed to create deployment package"

echo "Creating coupons_import_presigned_url function"
awslocal lambda create-function \
    --function-name "coupons_import_presigned_url" \
    --runtime "nodejs18.x" \
    --zip-file fileb://coupons_import_presigned_url.zip \
    --handler "index.handler" \
    --role "arn:aws:iam::000000000000:role/coupons_production_role" \
    --memory-size 128

[ $? == 0 ] || fail 3 "Failed to create function"
echo "coupons_import_presigned_url function created successfully"

#update lambda function
awslocal lambda update-function-code --function-name coupons_import_presigned_url --zip-file fileb://coupons_import_presigned_url.zip
echo "Lambda function 'coupons_import_presigned_url' updated with new code."

