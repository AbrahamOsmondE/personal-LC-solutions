# Leetcode Solutions
Repo containing automatically-uploaded LeetCode solutions of mine to track my progress (The solution gets committed only if the answer is correct). This is also just me trying my hands on GitHub Actions and Chrome extensions, and most definitely not a project designed for stat-padding Github stats.

# How it works
There are 3 parts to this project
- [x] Private Chrome extension that captures the LeetCode solution and other relevant information and passes it to AWS Lambda for processing, written in JS
- [x] AWS Lambda function which receives input from the Chrome extension and saves the solution into a file with the correct file type, and generates a `README.md` file containing more information on the LeetCode problem. These 2 files get dumped into s3, and their paths grouped based on their difficulty
- [x] Github Actions CRON job that runs everytime S3 gets updated.

## Chrome Extension
Written in TypeScript. A script with a bunch of `document.querySelector`, and checks when a leetcode solution is Accepted, and if it is do a POST request to the lambda function URL

## Lambda
Gets the request from the chrome extension, and dumps the data to S3. It will then call an endpoint to trigger the Github Actions

## Github Actions
Copies the file from s3 and push to `main`
