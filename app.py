import os.path

# import tornado.httpserver
import tornado
# import tornado.options
import tornado.web
from tornado.options import define, options

from function import jenkins
from url import url

define("port", default=801, help='Run on the given port', type=int)
define("url", group='jenkins')
define("user", group='jenkins')
define("passwd", group='jenkins')
define("base_dir", group='jenkins')

class Application(tornado.web.Application):
    def __init__(self):
        self.jenkins = jenkins.Jenkins

        handlers = url
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static")
        }

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    options.parse_config_file('./conf/server.conf')
    options.parse_command_line()

    # app = tornado.web.Application(
    #     # autoreload=True,
    #     handlers = url,
    #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
    #     static_path=os.path.join(os.path.dirname(__file__), "static")
    # )
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    print 'Server started...'
