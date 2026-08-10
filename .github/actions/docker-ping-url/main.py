import time
import requests
import os

def ping_url(url, delay, max_trials):
    trials = 0

    while trials < max_trials:
        response = requests.get(url)

        if response.status_code == 200:
            return True

        # show "retrying..." only if there will be another trial
        more_retries = trials < (max_trials - 1)
        print(f"Tried to ping {url} but failed{', retrying...' if more_retries else ''}")
        time.sleep(delay)
        trials += 1

    return False

import os

def run():
    url = os.environ["INPUT_URL"]
    delay = int(os.environ["INPUT_DELAY"])
    max_trials = int(os.environ["INPUT_MAX_TRIALS"])

    success = ping_url(url, delay, max_trials)

    if not success:
        raise Exception(f"Failed to ping {url}")
    else:
        print('All good!')

if __name__ == "__main__":
    run()