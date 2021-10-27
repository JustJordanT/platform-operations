import json
import os
import requests
import sys
# import pprint
from dotenv import load_dotenv, find_dotenv

# VARS
org = 'Basis-Theory'
API_URL = "https://api.github.com/"

# LOAD SECRETS
load_dotenv(find_dotenv())
GH_TOKEN = os.getenv('GH_TOKEN')
SLACK_HOOK = os.getenv('SLACK_HOOK')

authorization = f'token {GH_TOKEN}'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": authorization,
}

repo_info = requests.get(f"{API_URL}/orgs/{org}/repos", headers=headers)
repositories = repo_info.json()


def slack_test ():
    url = SLACK_HOOK
    message = f"{failures}"
    title = (f"New Incoming Alert :zap:")
    slack_data = {
        "username": "Repo-Alerts",
        "icon_emoji": ":car:",
        "channel": "#ID",
        "attachments": [
            {
                "color": "#ff0000",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


def check_repo(repo):
    repo_out_of_compliance = []
    # try:
    #     if repo.get("visibility") == "private":
    # print(repo_out_of_compliance)
    data = {
                "default_branch": 'master',
                "has_wiki": True,
                # "has_projects": True,
                "has_issues": False,
                "delete_branch_on_merge": True,
                "has_downloads": False,
                "has_issues": False,
                "has_wiki": False,
                # "VulnerabilityAlerts": True,
                }
    requests.patch(f"{API_URL}repos/basis-theory/{repo}/", headers=headers, json=data)
    repo_out_of_compliance.append(repo)
    return repo_out_of_compliance
    # except AttributeError:
    #     pass

        # requests.patch(REPOS_URL, headers=headers, json=data)
        # requests.patch(REPOS_URL, headers=headers, json=data)



repo_list = ['basistheory-private-test-1', 'basistheory-private-test-2']

for repo in repo_list:
    failures = check_repo(repo)
    # if failures:
    print(failures)
        # slack_test()
