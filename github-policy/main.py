import json
import requests
from Patch_Repo import patch_repo

repo_file = open("repos.json")

List = []

for repo in repo_file:
    # [List.strip() for i in List] //TODO Look into this list comp and see if this is something that we can use istead of the append method.
    List.append(repo.replace("\n", ""))
    # patch_repo(List)


for x in List:
    patch_repo(x)
