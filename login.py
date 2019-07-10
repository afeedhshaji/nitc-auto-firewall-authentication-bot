import pandas as pd
import requests
import time

class login:
    logged_in = 0
    URL = 'http://msftconnecttest.com'
    
    def login(username, password):
        while(1):
            try:
                r = requests.get(url = URL, verify=False)
                break
            except Exception as e:
                #pass
                print(e)

        magic = r.url.split('?')[1]
        r = requests.post(url=URL,
                          {'username': username, 'password': password, 'magic': magic, '4Tredir': URL})
        if 'keepalive' in r.url:
            logged_in = 1
