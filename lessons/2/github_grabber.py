import requests
from pprint import pprint

API_TOKEN = "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"  # until 02.10.2021
owner = "tishyk"
repo = "Pyro5"
query_url = f"https://api.github.com/repos/{owner}/{repo}"
params = {"state": "open", }
headers = {'Authorization': f'token {API_TOKEN}'}
r = requests.get(query_url, headers=headers, params=params)

json_data = r.json()

if __name__ == "__main__":
    pprint(json_data)

