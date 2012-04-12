#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gregory Sitnin <sitnin@gmail.com>"
__copyright__ = "Gregory Sitnin, 2011"
__version__ = "1.1.0"

import sys
import locale
import logging
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import define, parse_config_file, parse_command_line, options


class Home(tornado.web.RequestHandler):
    def get(self):
        self.render("site_home.html")


if __name__ == "__main__":
    urls = [
        ("/", Home),
    ]

    define("debug", type=bool, default=False)
    define("domain")
    define("bind_host")
    define("bind_port", type=int)
    define("locale", default="en_US")
    define("templates_path")

    parse_config_file(sys.argv[1])
    parse_command_line()

    locale.setlocale(locale.LC_ALL, "%s.UTF-8" % options.locale)
    reload(sys)
    sys.setdefaultencoding('utf-8')

    logging.info("Starting %s webapp in a %s mode" % (options.domain, "debug" if options.debug else "production"))

    settings = dict(
        debug=options.debug,
        template_path=options.templates_path,
        autoescape=None,
    )

    http_server = tornado.httpserver.HTTPServer(tornado.web.Application(urls, **settings), xheaders=True)
    http_server.listen(options.bind_port, options.bind_host)
    logging.info("Server version %s binded to %s:%d" % (__version__, options.bind_host, options.bind_port))

    logging.info("Starting I/O loop to serve requests...")
    tornado.ioloop.IOLoop.instance().start()
