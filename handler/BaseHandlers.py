# coding: utf-8

import os
import json
import ConfigParser
import logging

# import tornado
import tornado.web
import tornado.websocket

from tornado.options import define, options

logger = logging.getLogger(__name__)


class MyConfigParser(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr


# read the config file
def parse_config():
    cp = MyConfigParser(allow_no_value=True)
    cp.read('conf/apps.conf')
    protypes = {}
    protypes['soa'] = cp.options('soa')
    protypes['web'] = cp.options('web')
    return protypes


class Console(tornado.web.RequestHandler):
    def get(self):
        self.render('console.html')


class WebUpHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, message):
        data = json.loads(message)
        filelist = data['web_txtarea_after']
        isreboot = data['web_radio_isreboot']
        app = data['web_input_app']
        logger.info(isreboot)
        logger.info(type(filelist))
        self.write_message(filelist)

        jks = options.group_dict('jenkins')
        jk = self.application.jenkins(url=jks['url'], username=jks['user'], password=jks['passwd'])
        # result: SUCCESS, FAILURE
        result = jk.build(app, self.write_message)

        logger.info(result)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        protypes = parse_config()
        self.render('index.html', protypes=protypes)


class IsExist(tornado.web.RequestHandler):
    def post(self):
        app = self.get_argument('app')
        filelist = self.get_argument('filelist')
        filelist = filelist.split('\n')

        notexist = []
        for file in filelist:
            file_path = os.path.join('e:\\', app, file)
            if not os.path.isfile(file_path):
                notexist.append(file_path)

        if notexist:
            cb = {"status_code": 405, "filelist": notexist}
        else:
            cb = {"status_code": 200}
        self.write(cb)
