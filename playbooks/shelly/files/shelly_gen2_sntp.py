#!/usr/bin/env python3
import sys
import requests
from requests.auth import HTTPDigestAuth
import json

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
ntp_server = sys.argv[4]

auth = HTTPDigestAuth(user, password)

# Aktuelle Konfiguration lesen
r = requests.post(
    f'http://{host}/rpc',
    json={'id':1,'method':'Sys.GetConfig','params':{}},
    auth=auth,
    timeout=10
)
current = r.json()
current_server = current.get('result', {}).get('sntp', {}).get('server', '')

if current_server == ntp_server:
    print(json.dumps({'changed': False, 'msg': f'Timeserver bereits korrekt: {current_server}'}))
    sys.exit(0)

# Nur setzen wenn abweichend
r = requests.post(
    f'http://{host}/rpc',
    json={'id':1,'method':'Sys.SetConfig','params':{'config':{'sntp':{'server':ntp_server}}}},
    auth=auth,
    timeout=10
)
result = r.json()
result['changed'] = True
result['old_server'] = current_server
result['new_server'] = ntp_server
print(json.dumps(result))
