import requests
import json
import os
import pprint
from secrets import TOKEN
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
GH_TOKEN = os.getenv('GH_TOKEN')
# SLACK_HOOK = os.getenv('SLACK_HOOK')

# VARS
org = 'Basis-Theory'
API_URL = "https://api.github.com/"

authorization = f'token {GH_TOKEN}'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": authorization,
    }

repo_info = requests.get(f"{API_URL}orgs/{org}/repos?type=private&per_page=100", headers=headers)
r_dict = repo_info.json()

# for repo in r_dict:
#     print(repo.get('owner'))

pprint.pprint(r_dict)
