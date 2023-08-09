# Leetcode Solutions
Repo containing automatically-uploaded LeetCode solutions of mine to track my progress (The solution gets committed only if the answer is correct). This is also just me trying my hands on GitHub Actions and Chrome extensions, and most definitely not a project designed for stat-padding Github stats.

# How it works
There are 3 parts to this project
- [x] Private Chrome extension that captures the LeetCode solution and other relevant information and passes it to AWS Lambda for processing, written in JS
- [x] AWS Lambda function which receives input from the Chrome extension and saves the solution into a file with the correct file type, and generates a `README.md` file containing more information on the LeetCode problem. These 2 files get dumped into s3, and their paths grouped based on their difficulty
- [x] Github Actions workflow that runs whenever we upload a solution to s3

# Installation Guide
This acts as a rough guide on how to setup the chrome extension, lambda function and github actions if you would like to use this

## Pre-requisites
- AWS Account
- Github Account

## Chrome Extension
[Chrome Extension Installation Guide](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/)
Upload the `dist` to run the chrome extension. You would need to run `npm run build` to see changes to your code getting reflected, along with the [reloading the extension](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/)

After making the lambda function, Change `LAMBDA_URL` to the Lambda Function URL

## Lambda
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

## Github Actions
Create a `.yaml` file within a `.github/workflows` folder on the root directory of your repository with the following code

```yaml
name: WORKFLOW_NAME # Can be named anything
on:
  repository_dispatch: # To allow api calls to trigger this workflow
  workflow_dispatch: # To test the workflow from your repository page

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - uses: keithweaver/aws-s3-github-action@v1.0.0
        name: cp folder
        with:
          command: cp
          source: s3://YOUR_BUCKET_NAME/YOUR_FOLDER_NAME/ #Change to your bucket name (folder name refers to the folder inside your s3 bucket, optional)
          destination: ./solutions/ #folder name in your github repository
          aws_access_key_id: ${{ secrets.AWS_ACCESS_KEY_ID }} #DONT CHANGE instead configure on your repository page --> Settings --> Secrets and Variables --> Actions
          aws_secret_access_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }} #DONT CHANGE instead configure on your repository page --> Settings --> Secrets and Variables --> Actions
          aws_region: ap-southeast-1 # Change to your AWS region
          flags: --recursive
      - name: Commit changes
        env:
            TITLE: ${{ github.event.client_payload.title }}
        run: |
         git config --local user.email "YOUR_EMAIL"
         git config --local user.name "YOUR_USERNAME"
         git add .
         git diff-index --quiet HEAD || git commit -m "Upload Solution for $TITLE" -a
         git push origin main
```
