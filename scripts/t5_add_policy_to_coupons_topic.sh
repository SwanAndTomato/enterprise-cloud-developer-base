#!/bin/bash

awslocal sns set-topic-attributes \
  --topic-arn arn:aws:sns:us-east-1:000000000000:coupons \
  --attribute-name Policy \
  --attribute-value '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Principal": "*",
        "Action": "SNS:Publish",
        "Resource": "arn:aws:sns:us-east-1:000000000000:coupons",
        "Condition": {
          "StringNotEquals": {
            "SNS:Protocol": "email"
          }
        }
      }
    ]
  }'
