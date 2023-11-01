import requests, time, os

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

def last_updated(repo):
    url = f'https://api.github.com/repos/{repo}'
    response = requests.get(url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    if response.status_code == 200:
        updated = response.json()['pushed_at']
        t = time.mktime(time.strptime(updated, '%Y-%m-%dT%H:%M:%SZ'))
        # eastern standard time hack, fix asap
        return int(t) - 60*60*4
    else:
        return None