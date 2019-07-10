import pandas as pd
import requests
import time
import random


class login:
    logged_in = 0

    def login(username, password):
    list = ['http://msfconnect.com/redirect',
            'http://msfconnecttest.com/redirect', 'http://msn.com/redirect']

    while(1):
        try:
            p = random.choice(list)
            r = requests.get(p, verify=False)
            break
        except Exception as e:
            pass

    magic = r.url.split('?')[1]
    r = requests.post('http://msfconnect.com/',
                      {'username': username, 'password': password, 'magic': magic, '4Tredir': p})
    if 'keepalive' in r.url:
        logged_in = 1
