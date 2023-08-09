# Installation Guide
This will only describe a rough guide on how to setup the lambda function
## Pre-requisites
- AWS Account
- Github Account
## Steps
### 1. Create a new S3 Bucket and Lambda function
- Create the S3 Bucket
- Create the Lambda Function
  - When creating, click advanced settings --> Enable function URL --> Auth type NONE
  - Enable Function URL (This will be the URL used in the chrome extension code)
    - Set Allow Origin:   https://leetcode.com
    - Set Allow headers:  accept, content-type
    - Set Allow methods:  POST
  - Add Environment Variables:
    - GITHUB_REPO:  Github repository where you would like the solutions to be uploaded to
    - GITHUB_TOKEN: Github personal access token with `repo` and `workflow` scopes
    - GITHUB_USER:  Your github username
  - Add the following permission `Allow: s3:PutObject` linked to your bucket ARN

### 2. Upload your lambda function
Run the following commands on this `lambda-handler` folder

```
mkdir package
pip install --target ./package requests==2.28.2
cd package
zip -r ../my_deployment_package.zip .
cd ..
zip my_deployment_package.zip lambda_function.py
```

Then upload the `my_deployment_package.zip` to your lambda function dashboard (Code --> Upload from --> .zip file)

### 3. Configure github
- Create an AWS Access Key and AWS Secret Key with CLI scope, and add it to your repository secret (Under Settings section of your repository)



