# Leetcode Solutions
Just a repo containing my own automatically-uploaded LeetCode solutions to track my progress (The solution gets committed only if the answer is correct). This is also just me trying my hands on GitHub Actions, and definitely not a project designed for stat-padding

# How it works
There are 3 parts to this project
- [ ] Private Chrome extension that captures the LeetCode solution and other relevant information and passes it to AWS Lambda for processing, written in JS
- [ ] AWS Lambda function which receives input from the Chrome extension and saves the solution into a file with the correct file type, and generates a `README.md` file containing more information on the LeetCode problem. These 2 files get dumped into s3, and their paths grouped based on their difficulty
- [ ] Github Actions CRON job that runs daily copying every file within s3 and committing it into main.

## Chrome Extension

## Lambda

## Github Actions

