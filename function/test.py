import requests
import re
import sys

login_data = {
    'j_username': 'admin',
    'j_password': 'admin.123'
}
s = requests.Session()
try:
    s.get('http://192.168.1.223:8080/login?from=%2F', timeout=10)
    r = s.post('http://192.168.1.223:8080/j_acegi_security_check', data=login_data, timeout=10)
    cont = r.text
except requests.exceptions.ConnectionError, e:
    print 'error'
    sys.exit(1)

if re.findall(r'<title>Login Error', cont):
    print 'Login Failed'