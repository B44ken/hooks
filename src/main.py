import service_github

import time, json, os

config = json.load(open('hooks.json'))

def update_from_file():
    config = json.load(open('hooks.json'))
    for hook in config:
        if hook['service'] == 'github':
            last_updated = service_github.last_updated(hook['repo'])
            last_run = hook.get('lastRun', 0)
            if service_github.last_updated(hook['repo']) < last_run:
                continue
            print(f'updating {hook["repo"]} ')
            hook['lastRun'] = int(time.time())
            try:
                os.system(hook['command'])
                json.dump(config, open('hooks.json', 'w'), indent=4)
            except:
                print(f'error running {hook["command"]}')

if __name__ == '__main__':
    while True:
        update_from_file()
        time.sleep(15)