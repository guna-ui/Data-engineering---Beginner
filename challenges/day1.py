import requests
import json
from typing import Dict,Any


def fetch_git_repos(username,pagenumber,per_page)->Dict[str,Any]:
    for i in pagenumber:
      url=f'https://api.github.com/users/{username}/repos?page={i}&per_page={per_page}'
      response=requests.get(url)
      response.raise_for_status()
    #   print(json.dumps(response.json(),indent=2))
      user_data=response.json()
      return user_data



get_user_details=fetch_git_repos('octocat',pagenumber=[1,2],per_page=50)



user_array=[]

for i in range(len(get_user_details)):
     user_details={
     "name":get_user_details[i]["name"],
     "language":get_user_details[i]["language"],
     "stargazers_count":get_user_details[i]["stargazers_count"],
     'forks_count':get_user_details[i]['forks_count']
     }
     user_array.append(user_details)

print(json.dumps(user_array,indent=2))
