#!/bin/bash

# Create the IAM role with a trust policy that allows Lambda to assume this role
aws --endpoint-url=http://localhost:4566 iam create-role \
    --role-name coupons_lambda_role \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": {
        "Effect": "Allow",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    }'

# Attach permissions to the role to allow CloudWatch logging and DynamoDB access
aws --endpoint-url=http://localhost:4566 iam put-role-policy \
    --role-name coupons_lambda_role \
    --policy-name coupons_lambda_policy \
    --policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource": "arn:aws:logs:us-east-1:000000000000:log-group:/aws/lambda/coupons*"
        },
        {
          "Effect": "Allow",
          "Action": [
            "dynamodb:PutItem",
            "dynamodb:GetItem",
            "dynamodb:Scan",
            "dynamodb:Query"
          ],
          "Resource": "arn:aws:dynamodb:us-east-1:000000000000:table/coupons"
        }
      ]
    }'
