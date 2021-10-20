import json
import requests
import pprint
# from secrets import TOKEN

# VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
REPOS_URL = f"{BASE_URL}users/{USER}/repos"


# Passing PATCH data into API calls
# data = {
#     "name": "mix123456",
#     "has_wiki": True,x
#     "has_projects": False,
#     "has_issues": False
# }


headers = {
    'Accept': 'token' + TOKEN,
    'Authorization': 'token %s' % TOKEN,
}

repo_info = requests.get(REPOS_URL, headers=headers)
r_dict = repo_info.json()


def check_wiki ():
    for repo in r_dict:
        if repo.get('has_wiki'):
            # print(repo.get('name'), 'Has wiki feature enabled' ,repo.get('has_wiki'))
            print('[', repo.get('name'), ']', 'Has wiki feature enabled')
            # print('This is true')


def check_issues ():
    for repo in r_dict:
        if repo.get('has_issues'):
            print('[', repo.get('name'), ']', 'Has issues feature enabled')


def check_project ():
    for repo in r_dict:
        if repo.get('has_projects'):
            print('[', repo.get('name'), ']', 'Has issues feature enabled')


check_issues()

check_wiki()
