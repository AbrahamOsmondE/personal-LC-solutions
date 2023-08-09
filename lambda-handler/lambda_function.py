import boto3
import json
import requests
import time
import os

def lambda_handler(event, context):
    GITHUB_USER = os.environ.get('GITHUB_USER')
    GITHUB_REPO = os.environ.get('GITHUB_REPO')
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

    try:
        request_body = json.loads(event['body'])
        title = request_body['title']
        difficulty = request_body['difficulty']
        code_answer = request_body['code_answer']
        readme = request_body['readme']
        
        encoded_readme = readme.encode("utf-8")
        encoded_solution = code_answer.encode("utf-8")

        bucket_name = "" #YOUR BUCKET NAME
        folder_name = "" #YOUR FOLDER NAME (optional), remove if its on bucket root
        readme_file_name = "README.md"
        solution_file_name = "solutions.py"
        s3 = boto3.resource("s3")
        s3_readme_file_name = f"{folder_name}/{difficulty}/{title}/" + readme_file_name
        s3_solution_file_name = f"{folder_name}/{difficulty}/{title}/" + solution_file_name

        s3.Bucket(bucket_name).put_object(Key=s3_readme_file_name, Body=encoded_readme)
        s3.Bucket(bucket_name).put_object(Key=s3_solution_file_name, Body=encoded_solution)
        time.sleep(5)
        url = f'https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/dispatches'
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {GITHUB_TOKEN}',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        payload = {
            'event_type': 'on-demand-test',
            'client_payload': {'title': title}
        }

        response = requests.post(url, headers=headers, json=payload)
        return {
            'statusCode': 200,
            'body': "Success"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }