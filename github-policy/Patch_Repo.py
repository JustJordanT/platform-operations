import requests
import pprint
import os
from dotenv import load_dotenv, find_dotenv
import json
import sys

load_dotenv(find_dotenv())
GH_TOKEN = os.getenv('GH_TOKEN')
SLACK_HOOK = os.getenv('SLACK_HOOK')


# print(os.getenv('SLACK_HOOK'))


def patch_repo ():
    # VARS
    USER = 'justjordant'
    BASE_URL = "https://api.github.com/"
    # REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
    # REPOS_URL = f"{BASE_URL}repos/{USER}/{repo_name}"
    REPOS_URL = f"{BASE_URL}repos/{USER}/repos"

    jada = {
        "has_wiki": True,
        "has_projects": True,
        "has_issues": True,
        "ArchiveOnDestroy": True,

    }

    headers = {
        'Accept': 'access_token' + GH_TOKEN,
        'Authorization': 'token %s' % GH_TOKEN,
    }

    repo_info = requests.patch(REPOS_URL, headers=headers, json=jada)
    r = repo_info.json()

    # parsed = json.loads(repo_info)

    # pprint.pprint(repo_info)
    pprint.pprint(r)


patch_repo()
