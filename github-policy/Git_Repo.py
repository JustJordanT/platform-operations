# import github
import requests
import pprint
# from secrets import GITHUB_TOKEN
import urllib3
import urlopen
from secrets import TOKEN

# token = "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"
# API_URL = "https://api.github.com"
# payload = '{"name": "justjordant"}'
# # headers = {
# #     "Accept": "application/vnd.github.v3+json",
# #     "Authorization": "token" + GITHUB_TOKEN
# # }
#
# headers = {'Authorization': 'token ' + token}
#
# login = requests.get('https://api.github.com/', 'justjordant/', headers=headers)
# print(login.json())


url = "https://api.github.com/users/justjordant/repos"
TOKEN = "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"

request = Request(url)
request.add_header('Authorization', 'token %s' % TOKEN)
response = urlopen(request)
print(response.read())
