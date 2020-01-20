import subprocess
import requests
import time


def login(gatewayaddr, magic):

    logged_in = 0

    details = {"B17001AB":"dummypassword", "B17002AB", "dummypassword"}
    for key in details:
        roll_no = key
        dob = details[key]

        url_a = '{}/login?{}'.format(gatewayaddr, magic)

        r = requests.post(url_a,
                          {'username': roll_no, 'password': dob, 'magic': magic, '4Tredir': url_a})

        if 'keepalive' in r.url:
            print(roll_no+":"+dob)
            logout(gatewayaddr, magic)
            break


def logout(gateway_addr, magic):

    logout_url = "{}/logout?{}".format(gateway_addr, magic)
    requests.get(logout_url)
    # print(r.url)

if __name__ == "__main__":
    cmd =  'ip r | grep "default" | cut -d" " -f3'
    ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    ip_addr = output[:-1].decode("utf-8")
    
    port = "1000"

    gateway_addr = "http://{}:{}".format(ip_addr, port)

    res = requests.get('http://www.msftconnecttest.com/')

    magic = "0c0708000b16e15e"

    if('connecttest.txt' in res.text):
        print("Already logged in")
        print("Do you want to logout?\n1. Press 1 to logout.\n2. Press 2 to cancel logout\n")
        opt = int(input())
        if (opt == 1):
            logout(gateway_addr, magic)
        else:
            print("Skipping logout")
            exit(0)
            
            
    res = requests.get('http://www.msftconnecttest.com/')
    magic = res.url.split('?')[1]
    login(gateway_addr, magic)
