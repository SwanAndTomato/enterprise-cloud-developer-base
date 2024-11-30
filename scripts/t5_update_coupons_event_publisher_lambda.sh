#!/bin/bash

awslocal lambda update-function-code \
  --function-name coupons_event_publisher \
  --zip-file fileb://path/to/your/lambda_function.zip
