#!/bin/bash

awslocal s3api put-bucket-policy --bucket coupons --policy '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceMFADelete",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:DeleteObject",
      "Resource": "arn:aws:s3:::coupons/*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}'
echo "Bucket policy added to 'coupons' bucket to enforce MFA delete."
