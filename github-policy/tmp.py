import json
import os
import requests
import sys
# import pprint
from dotenv import load_dotenv, find_dotenv

# VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
# REPOS_URL = f"{BASE_URL}users/{USER}/repos?per_page=100"
REPOS_URL = f"{BASE_URL}users/{USER}/repos"

# jada = {
#     "name": "mix123456",
#     "has_wiki": True,
#     "has_projects": False,
#     "has_issues": False
# }

load_dotenv(find_dotenv())
GH_TOKEN = os.getenv('GH_TOKEN')
SLACK_HOOK = os.getenv('SLACK_HOOK')
print(os.getenv('SLACK_HOOK'))


headers = {
    'Accept': 'token' + GH_TOKEN,
    'Authorization': 'token %s' % GH_TOKEN,
}

repo_info = requests.get(REPOS_URL, headers=headers)
r_dict = repo_info.json()


# parsed = json.loads(repo_info)

def check_wiki ():
    for repo in r_dict:
        try:
            if repo.get('has_wiki'):
                return f"{repo.get('name')} -' Has wiki feature enabled\'"
            # print('This is true')
        except AttributeError:
            pass


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


def slack_test (check_name):
    url = SLACK_HOOK
    message = check_name
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


# pprint.pprint(repo_info)
# repos = [r]
# repos = r.json()

# for repo in repo_info:
#     for attribute,value in repo.iteritems():
#         print(attribute,value)

# repos["private"]

# for repo in repos:
#     print(repo)

# check_issues()

# check_wiki()

slack_test(check_wiki())
