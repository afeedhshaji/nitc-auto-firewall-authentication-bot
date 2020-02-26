import requests
import subprocess


headers = \
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}


def login(uname, passw):
    url_1 = 'http://www.google.com'
    session = requests.Session()
    res = session.get(url_1, headers=headers)
    magic = res.url.split('?')[1]
    url_2 = res.url
    payload = {
        '4Tredir': 'http://google.com/',
        'username': uname,
        'password': passw,
        'magic': str(magic),
    }
    res = requests.post(url_2, headers=headers, data=payload)
    # print res.text
    if 'Failed' in res.text:
        print(uname + 'failed')
        return False
    else:
        print(uname + ':' + passw)
        print(res.url)
        return True


def main():

    cmd = 'ip r | grep "default" | cut -d" " -f3'
    ps = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    ip_addr = output[:-1].decode("utf-8")
    # print(ip_addr)

    port = "1000"

    print("Checking connectivity..")
    try:
        res = requests.head('http://www.google.co.in')
        print('Already connected. :)')
        requests.get(
            url='http://'+ip_addr+':'+port+'/logout?0c0a0e0a0a1fea52', headers=headers)
        print("Logged out successfully")
    except requests.ConnectionError:

        details = {'uname1' : 'passw1', 'uname2' : 'passwd2'}
        for key in cache:
            username = key
            password = details[key]
            if login(username, password):
                # r = get(
                    # url="http://172.16.12.1:1000/logout?0c0a0e0a0a1fea52", headers=headers)
                print("Logged in")
                exit(0)
            else:
                pass

        for key in details:
            username = key
            password = details[key]
            if login(username, password):
                # r = get(
                    # url="http://172.16.12.1:1000/logout?0c0a0e0a0a1fea52", headers=headers)
                print("Logged in")
                break
            else:
                pass


if __name__ == '__main__':
    main()
