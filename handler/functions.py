# coding: utf-8

import re
import jenkinsapi

from jenkinsapi.jenkins import Jenkins
from jenkinsapi.api import search_artifact_by_regexp
from jenkinsapi.build import Build

jk = Jenkins('http://192.168.1.218:8080', username='admin', password='admin')

# jk.build_job('mkt-bg')

ids = re.compile(r'mkt-bg-.*.war')

result = search_artifact_by_regexp('http://192.168.1.218:8080', username='admin', password='admin', jobid='mkt-bg', artifactRegExp=ids)

print result