#!/bin/bash

awslocal lambda update-function-code \
  --function-name coupons_notification_sender \
  --zip-file fileb://path/to/your/lambda_function.zip
