#!/usr/bin/env python3
import sys
import requests
from requests.auth import HTTPDigestAuth
import json

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
ntp_server = sys.argv[4]

r = requests.post(
    f'http://{host}/rpc',
    json={'id':1,'method':'Sys.SetConfig','params':{'config':{'sntp':{'server':ntp_server}}}},
    auth=HTTPDigestAuth(user, password),
    timeout=10
)
print(r.text)
