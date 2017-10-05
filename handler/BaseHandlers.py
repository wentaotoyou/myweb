# coding: utf-8

import tornado
import tornado.web
import os
import ConfigParser


class MyConfigParser(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr


def parse_config():
    # config_file = os.path.join(__file__, './config)
    cp = MyConfigParser(allow_no_value=True)
    cp.read('conf/myweb.conf')
    protypes = {}
    protypes['soa'] = cp.options('soa')
    protypes['web'] = cp.options('web')
    return protypes


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        protypes = parse_config()
        self.render('index.html', protypes=protypes)


class WebUpdate(tornado.web.RequestHandler):
    def post(self):
        isupdate = self.get_argument('isupdate')
        app = self.get_argument('web_input_app')
        filelist = self.get_argument('web_txtarea_after')
        filelist = filelist.split('\n')

        notexist = []
        for file in filelist:
            file_path = os.path.join('/data/web', app, file)
            if not os.path.isfile(file_path):
                notexist.append(file_path)

        if notexist:
            cb = {"status_code": 405, "filelist": notexist}
        else:
            cb = {"status_code": 200}

        print cb
        self.write(cb)
