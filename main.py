import requests
import json
from typing import Dict,Any


def fetch_github_user_data(username:str)->Dict[str,Any]:
    url=f"https://api.github.com/users/{username}"
    response=requests.get(url)
    response.raise_for_status()
    user_data:Dict[str,Any] =response.json()
    return user_data


#Fetch Data
git_user=fetch_github_user_data("octocat")

##Pretty-print full the dictionary
print(json.dumps(fetch_github_user_data("octocat"),indent=2))

name=git_user["name"]

public_repos=git_user["public_repos"]

company=git_user.get("company","not specified")

bio=git_user.get("bio",'N/A')

print(f"\nusername {name} has {public_repos} repository")
print(f"\ncompany name is{company}")
print(f"\nbio name is {bio}")
