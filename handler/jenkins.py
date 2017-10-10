# coding: utf-8

import re
import time
import requests

class Jenkins():
    def __init__(self, url, username, password):
        self._url = url

        jk_index = self._url + '/login?from=%2F'
        login_url = self._url + '/j_acegi_security_check'

        login_data = {
            'j_username': username,
            'j_password': password,
        }

        session = requests.Session()
        session.get(jk_index)
        session.post(login_url, data=login_data)

        self.__session = session

    def job_info(self, app):
        base_url = self._url
        info_url = base_url + '/job/mkt-bg/api/json'

        s = self.__session
        r = s.get(info_url)
        res = r.json()
        job_info  = {
            # 随用随添加
            'nextBuildNumber': res['nextBuildNumber'],
            'buildable': res['buildable'],
            'inQueue': res['inQueue'],
            'keepDependencies': res['keepDependencies'],
            'queueItem': res['queueItem'],
            'concurrentBuild': res['concurrentBuild']
        }

        return job_info


    def build(self, app):
        app = app
        base_url = self._url
        job_url = base_url + '/job/%s' % app
        build_url = base_url + '/job/%s/build' % app

        # next build number
        nbn = self.job_info(app)['nextBuildNumber']
        print nbn

        s = self.__session
        r_build = s.post(build_url)
        if r_build.status_code != 201:
            return 555

        # 取日志 post
        # http://192.168.1.218:8080/job/mkt-bg/124/logText/progressiveHtml
        log_url = job_url + '/%s/logText/progressiveHtml' % nbn
        print log_url

        data_log = {'start': 0}
        sc = 404
        while sc == 404:
            res = s.post(log_url, data=data_log)
            sc = res.status_code
            print sc
            print res.text