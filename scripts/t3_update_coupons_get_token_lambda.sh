#!/bin/bash

awslocal lambda update-function-code \
    --function-name coupons_get_token \
    --zip-file fileb://coupons_get_token.zip
