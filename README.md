## save-json-api

A very simple Python script designed to be deployed as a an AWS Lambda function behind an API Gateway.

It takes a request body, validates it is JSON and then saves it to S3 using a random file name.

It echos back the request, but with an `id` field added which is the same random string as is used as the file name.

The random string is a uuidv4.