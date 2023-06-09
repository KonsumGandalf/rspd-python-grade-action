import json
import requests
import os
import re

# Import environmental variables
api_url = os.environ.get("API_URL")
repo_url = os.environ.get("REPO_URL")
repo = os.environ.get("REPO")
actor = os.environ.get("ACTOR")

with open('.report.json', 'r') as f:
    contents = f.read()
    # Remove all chars that could lead to errors
    contents = re.sub(r"[^\x20-\x7E]", "", contents)
    report_data = json.loads(contents)

data = {
    'repositoryUrl': repo_url,
    'actor': actor,
    'repository': repo,
    'submission': report_data
}

# Convert dictionary to JSON string
json_data = json.dumps(data)

# Send POST request to API_URL with JSON data
response = requests.post(api_url, json=data)