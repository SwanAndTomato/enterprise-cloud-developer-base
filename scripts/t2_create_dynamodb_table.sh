#!/bin/bash

# Create a DynamoDB table named 'coupons'
aws --endpoint-url=http://localhost:4566 dynamodb create-table \
    --table-name coupons \
    --attribute-definitions \
        AttributeName=id,AttributeType=S \
    --key-schema \
        AttributeName=id,KeyType=HASH \
    --provisioned-throughput \
        ReadCapacityUnits=50,WriteCapacityUnits=10