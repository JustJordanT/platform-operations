import requests
import pprint
from secrets import TOKEN

#VARS
USER = 'justjordant'
BASE_URL = "https://api.github.com/"
REPO_URL = f"https://api.github.com/repos/{USER}/JordanBlogSite"
REPOS_URL = f"{BASE_URL}users/{USER}/repos"


# r = requests.get("https://api.github.com/users/justjordant/repos")

headers = {
    'Accept': 'token' + TOKEN,
    'Authorization': 'token %s' % TOKEN
    }
repo_info = requests.get(REPOS_URL, headers=headers).json()

# pprint.pprint(repo_info)
# pprint.pprint(dir(repo_info))
pprint.pprint(repo_info)