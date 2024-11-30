#!/bin/bash

# Hash passwords

awslocal dynamodb put-item \
    --table-name users \
    --item '{"username": {"S": "tester1"}, "password": {"S": "<hashedValue1>"}}'

awslocal dynamodb put-item \
    --table-name users \
    --item '{"username": {"S": "tester2"}, "password": {"S": "<hashedValue2>"}}'
