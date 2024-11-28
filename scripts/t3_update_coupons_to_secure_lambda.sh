#!/bin/bash

awslocal lambda update-function-code \
    --function-name coupons_to_secure \
    --zip-file fileb://coupons_to_secure.zip
