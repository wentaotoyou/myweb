# coding: utf-8


import requests

url = 'http://192.168.1.218:8080'

r = requests.post('http://192.168.1.218:8080/view/mkt-server/job/mkt-bg/build', auth=('admin', 'admin'))

print r.headers
print r.status_code
print r.text
