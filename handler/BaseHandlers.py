# coding: utf-8

import os
import json
import ConfigParser
import tornado
import tornado.web
import tornado.websocket


class MyConfigParser(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr


# read the config file
def parse_config():
    cp = MyConfigParser(allow_no_value=True)
    cp.read('conf/myweb.conf')
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
        # self.write_message('copy that %s' % message)
        data = json.loads(message)
        print data
        filelist = data['web_txtarea_after']
        isreboot = data['web_radio_isreboot']
        app = data['web_input_app']
        print app

        jk = self.application.jenkins('http://192.168.1.218:8080', username='admin', password='admin')
        jk.build(app, self)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        protypes = parse_config()
        self.render('index.html', protypes=protypes)


class WebUpdate(tornado.web.RequestHandler):
    def post(self):
        app = self.get_argument('web_input_app')
        filelist = self.get_argument('web_txtarea_after')
        filelist = filelist.split('\n')


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
