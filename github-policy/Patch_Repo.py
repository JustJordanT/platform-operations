import requests
# import json
import pprint
from secrets import TOKEN


def patch_repo(repo_name):
    # VARS
    USER = 'justjordant'
    BASE_URL = "https://api.github.com/"
    # REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
    REPOS_URL = f"{BASE_URL}repos/{USER}/{repo_name}"

    jada = {
        # "name": {,
        "has_wiki": True,
        # "has_projects": False,
        # "has_issues": False
    }

    headers = {
        'Accept': 'token' + TOKEN,
        'Authorization': 'token %s' % TOKEN,
    }

    repo_info = requests.patch(REPOS_URL, headers=headers, json=jada)
    r = repo_info.json()

    # parsed = json.loads(repo_info)

    # pprint.pprint(repo_info)
    pprint.pprint(r)
patch_repo('platform-operations')