import requests
import time
import sys
from bs4 import BeautifulSoup
import numpy as np

def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua

user_agent = get_random_ua()
headers = {
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'user-agent':user_agent,
        'referer':referer
    }

response = requests.get('https://www.oneflare.com.au/b/martino-professional-cleaners',headers=headers,proxies={'https': proxy_url})

proxy = get_random_proxy().replace('\n', '')
        service_args = [
            '--proxy={0}'.format(proxy),
            '--proxy-type=http',
            '--proxy-auth=user:path'
        ]
        print('Processing..' + url)
        driver = webdriver.PhantomJS(service_args=service_args)