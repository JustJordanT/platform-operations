import requests
import json
import pprint
from secrets import TOKEN

#VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
# REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
REPOS_URL = f"{BASE_URL}repos/{USER}/MIXcms"


headers = {
    'Accept': 'token' + TOKEN,
    'Authorization': 'token %s' % TOKEN,
    'name': 'name' + "mix213"
    }

repo_info = requests.patch(REPOS_URL, headers=headers, json={"name": "mix123"})
r = repo_info.json()

# parsed = json.loads(repo_info)



# pprint.pprint(repo_info)
pprint.pprint(r)