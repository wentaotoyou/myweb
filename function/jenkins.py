# coding: utf-8

import re
import sys
import time
import logging
import requests

logger = logging.getLogger(__name__)

class Jenkins:
    def __init__(self, url, username, password):
        self._url = url

        jk_index = self._url + '/login?from=%2F'
        login_url = self._url + '/j_acegi_security_check'

        login_data = {
            'j_username': username,
            'j_password': password,
        }

        session = requests.Session()
        try:
            session.get(jk_index, timeout=10)
            r = session.post(login_url, data=login_data, timeout=10)
            cont = r.text
        except Exception, e:
            logger.error(e)
        logger.info(cont)

        self.__session = session

    def get_job_info(self, app):
        base_url = self._url
        info_url = base_url + '/job/%s/api/json' % app

        s = self.__session
        r = s.get(info_url)
        res = r.json()
        job_info = {
            # 随用随添加
            'nextBuildNumber': res['nextBuildNumber'],
            'buildable': res['buildable'],
            'inQueue': res['inQueue'],
            'queueItem': res['queueItem'],
        }

        xmlconfig = s.get(base_url + '/job/%s/config.xml' % app).text
        logger.info(base_url + '/job/%s/config.xml' % app)

        # <customWorkspace>/data/projects/web/mkt-server/mkt-bg</customWorkspace>
        workspace = re.findall(r'<customWorkspace>(.*?)</customWorkspace>', xmlconfig)[0]
        job_info['workspace'] = workspace
        return job_info

    def build(self, app, hd):
        ret_data = {} # 返回值
        hd = hd     # websocket 实例
        app = app
        base_url = self._url
        job_url = base_url + '/job/%s' % app
        build_url = base_url + '/job/%s/build' % app

        # next build number
        nbn = self.get_job_info(app)['nextBuildNumber']

        # print nbn
        # 查看指定编号的编绎信息
        # http://192.168.1.218:8080/job/eshop-wap/7/api/json?pretty=true
        result_url = job_url + '/%s/api/json' % nbn

        s = self.__session
        r_build = s.post(build_url)
        if r_build.status_code != 201:
            ret_data['result'] = "FAILURE"
            return ret_data

        # 取日志 post
        # http://192.168.1.218:8080/job/mkt-bg/124/logText/progressiveHtml
        log_url = job_url + '/%s/logText/progressiveHtml' % nbn

        inQueue = True
        while inQueue:
            job_info = self.get_job_info(app)
            inQueue = job_info.get('inQueue', False)
            time.sleep(3)

        def fetchlog(pos):
            res = s.post(log_url, data=pos)
            headers = res.headers

            if headers['Content-Length'] != 0:
                hd.write_message(res.text)
                pos = {'start': headers['X-Text-Size']}
                if headers.get('X-more-Data', False):
                    time.sleep(1)
                    fetchlog(pos)

        data_log = {'start': 0}
        fetchlog(data_log)

        result = s.get(result_url).json()['result']
        ret_data['result'] = result
        ret_data['workspace'] = job_info['workspace']
        return ret_data