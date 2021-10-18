import requests
import json
import pprint
from secrets import TOKEN

# VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
# REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
REPOS_URL = f"{BASE_URL}repos/{USER}/MIXcms"

headers = {
    'Accept': 'token' + TOKEN,
    'Authorization': 'token %s' % TOKEN,
}

repo_info = requests.get(REPOS_URL, headers=headers, json={"archived": "True"})
r = repo_info.json()

pprint.pprint(r)
