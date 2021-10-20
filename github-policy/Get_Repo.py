import requests
import json
import pprint
from secrets import TOKEN

# VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
# REPOS_URL = f"{BASE_URL}users/{USER}/repos?per_page=100"
REPOS_URL = f"{BASE_URL}users/{USER}/repos"

headers = {
    'Accept': 'token' + TOKEN,
    'Authorization': 'token %s' % TOKEN
    }

repo_info = requests.get(REPOS_URL, headers=headers)
r_dict = repo_info.json()

# parsed = json.loads(repo_info)


with open('data.json', 'w') as f:
    json.dump(repo_info, f)

# pprint.pprint(repo_info)
# print(r_dict)