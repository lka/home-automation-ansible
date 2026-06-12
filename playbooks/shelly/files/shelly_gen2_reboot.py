#!/usr/bin/env python3
import sys
import requests
from requests.auth import HTTPDigestAuth
import json

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

r = requests.post(
    f'http://{host}/rpc',
    json={'id':1,'method':'Shelly.Reboot','params':{}},
    auth=HTTPDigestAuth(user, password),
    timeout=10
)
print(json.dumps({'rebooted': True, 'host': host}))
