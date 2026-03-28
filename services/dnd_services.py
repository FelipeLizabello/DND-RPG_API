import requests

def get_dnd_races():
    url = "https://www.dnd5eapi.co/api/2014/races"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()