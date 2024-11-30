#!/bin/bash
awslocal s3api create-bucket --bucket coupons --acl private
echo "S3 bucket 'coupons' created with private ACL."
