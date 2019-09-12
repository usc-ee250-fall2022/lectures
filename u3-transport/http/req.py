import requests
import json

r = requests.get('https://api.github.com/orgs/usc-ee250-fall2019/repos')
if r.status_code == 200:
    repos = r.json()
    for repo in repos:
        print(repo['name'])
elif r.status_code == 404:
    print("URI not found")


