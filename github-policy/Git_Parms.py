import json
import requests
from secrets import TOKEN

#VARS
# USER = 'justjordant'
# BASE_URL = "https://api.github.com/"
# REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
REPOS_URL = f"{BASE_URL}users/{USER}/repos"

f = open('repos.json')

for repo in f:
    array = []
    array.append(str(repo))
    print(array)

# headers = {
#     'Accept': 'token' + TOKEN,
#     'Authorization': 'token %s' % TOKEN
#     }
# repo_info = requests.get(REPOS_URL, headers=headers).json()

