# coding: utf-8

import jenkins

jk = jenkins.Jenkins('http://192.168.1.218:8080', username='admin', password='admin')
r = jk.build('mkt-bg')
print r