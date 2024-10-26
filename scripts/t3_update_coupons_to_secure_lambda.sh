#!/bin/bash

aws --endpoint-url=http://localhost:4566 lambda update-function-code \
    --function-name coupons_to_secure \
    --zip-file fileb://coupons_to_secure_lambda.zip
