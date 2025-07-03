import requests
import json
import time
import random
from libs.phrase_api import get_all_projects, get_all_projects_strings

with open('config.json', 'r') as f:
    config = json.load(f)

access_token = config['phrase_token']

phrase_headers = {
    'Authorization': f'token {access_token}',
    'User-Agent': 'My Python App (contact@example.com)',  # Required header
    'Content-Type': 'application/json'
}

base_url="https://api.phrase.com/v2"

# Usage
projects = get_all_projects_strings(access_token, base_url)
print(f"Found {len(projects)} projects")

def update_project_keys(project_id):

for project in projects:
    project_name = project['name']
    project_id = project['id']

    print(f"Project: {project_name} (ID: {project_id})")
    if project_name == "web-language":
        update_project_keys(project_id)
