import json
import requests
import pprint
from secrets import TOKEN

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


headers = {
    'Accept': 'token' + TOKEN,
    'Authorization': 'token %s' % TOKEN,
}

repo_info = requests.get(REPOS_URL, headers=headers)
r_dict = repo_info.json()


# parsed = json.loads(repo_info)


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


# pprint.pprint(repo_info)
# repos = [r]
# repos = r.json()

# for repo in repo_info:
#     for attribute,value in repo.iteritems():
#         print(attribute,value)

# repos["private"]

# for repo in repos:
#     print(repo)

check_issues()

check_wiki()
