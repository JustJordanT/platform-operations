import json
import os
import requests
import sys
# import pprint
from dotenv import load_dotenv, find_dotenv

# VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
# REPOS_URL = f"{BASE_URL}users/{USER}/repos?per_page=100"
REPOS_URL = f"{BASE_URL}users/{USER}/repos"

# jada = {
#     "name": "mix123456",
#     "has_wiki": True,
#     "has_projects": False,
#     "has_issues": False
# }

load_dotenv()
GH_TOKEN = os.environ('GH_TOKEN')
SLACK_HOOK = os.environ('SLACK_HOOK')


headers = {
    'Accept': 'token' + GH_TOKEN,
    'Authorization': 'token %s' % GH_TOKEN,
}

repo_info = requests.get(REPOS_URL, headers=headers)
repositories = repo_info.json()


def slack_test ():
    url = SLACK_HOOK
    message = f"{failures}"
    title = (f"New Incoming Alert :zap:")
    slack_data = {
        "username": "Repo-Alerts",
        "icon_emoji": ":car:",
        # "channel" : "#general",
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

def check_repo (repo):
    repo_failures = []
    if repo.get('has_wiki'):
        # print(repo.get('has_wiki'))
        repo_failures.append(repo.get('has_wiki'))
    return repo_failures


for repo in repositories:
    failures = check_repo(repo)
    if failures:
        print(failures)
        slack_test()
        # (f"{repo.get('name')} -' Has wiki feature enabled'")


# def check_wiki ():
#     return blob
#             # print('This is true')
#         except AttributeError:
#             pass


# def check_issues ():
#     for repo in r_dict:
#         if repo.get('has_issues'):
#             print('[', repo.get('name'), ']', 'Has issues feature enabled')
#
#
# def check_project ():
#     for repo in r_dict:
#         if repo.get('has_projects'):
#             print('[', repo.get('name'), ']', 'Has issues feature enabled')








