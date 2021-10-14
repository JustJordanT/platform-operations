import requests
import pprint

#VARS
USER = 'justjordant'
REPO_URL = f"https://api.github.com/repos/{USER}/platform-operations"



# r = requests.get("https://api.github.com/users/justjordant/repos")
repo_info = requests.get(REPO_URL).json()

pprint.pprint(repo_info)