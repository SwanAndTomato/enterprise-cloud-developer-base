export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"

aws --endpoint-url=http://localhost:4566 lambda invoke \
  --function-name coupons_get_token \
  --cli-binary-format raw-in-base64-out \
  --payload '{"body": "{\"username\": \"tester1\", \"password\": \"Pc4RM0AMKy5aSGfD\"}"}' \
  outputfile.txt
