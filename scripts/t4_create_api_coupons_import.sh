#!/bin/bash

awslocal apigateway create-rest-api --name "CouponsAPI"
PARENT_ID=$(awslocal apigateway get-resources --rest-api-id <rest-api-id> --query 'items[0].id' --output text)

awslocal apigateway create-resource --rest-api-id <rest-api-id> --parent-id $PARENT_ID --path-part "coupons"
RESOURCE_ID=$(awslocal apigateway create-resource --rest-api-id <rest-api-id> --parent-id $PARENT_ID --path-part "import" --query 'id' --output text)

awslocal apigateway put-method --rest-api-id <rest-api-id> --resource-id $RESOURCE_ID --http-method POST --authorization-type NONE
awslocal apigateway put-integration --rest-api-id <rest-api-id> --resource-id $RESOURCE_ID --http-method POST --type AWS_PROXY --integration-http-method POST --uri "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:coupons_import/invocations"

awslocal apigateway create-deployment --rest-api-id <rest-api-id> --stage-name dev
