import requests, time

def last_updated(repo):
    url = f'https://api.github.com/repos/{repo}'
    response = requests.get(url)
    if response.status_code == 200:
        updated = response.json()['updated_at']
        return time.mktime(time.strptime(updated, '%Y-%m-%dT%H:%M:%SZ'))
    else:
        return None