#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gregory Sitnin <sitnin@gmail.com>"
__copyright__ = "Gregory Sitnin, 2011"
__version__ = "1.0"

import os
import sys
import json
import locale
import pprint
import logging
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import define, parse_config_file, parse_command_line, options
import tornado_tools


class Home(tornado.web.RequestHandler):
    def get(self):
        self.render("site_home.html")


if __name__ == "__main__":
    urls = [
        ("/", Home),
        tornado_tools.handlers.AppStatusUrl
    ]

    define("debug", type=bool, default=False)
    define("domain")
    define("bind_host")
    define("user", default="www-data")
    define("group", default="www-data")
    define("bind_port", type=int)
    define("session_timeout", type=int, default=15)
    define("locale", default="en_US")
    define("templates_path")


    def setup_uid(user, group, logfile):
        if os.getuid() != 0:
            logging.error("This service must be run with root privileges")
            return False
        else:
            if unicode(user).isdecimal():
                uid = int(user)
            else:
                import pwd
                uid = pwd.getpwnam(user)[2]
            if unicode(group).isdecimal():
                gid = int(group)
            else:
                import grp
                gid = grp.getgrnam(user)[2]
            if (uid == 0 or gid == 0):
                logging.error("Unknown user or group: %s/%s"%(user, group))
            else:
                if logfile:
                    os.chown(logfile, uid, gid)
                os.setgid(gid)
                os.setuid(uid)
                return False
        return True


    parse_config_file(sys.argv[1])
    parse_command_line()

    locale.setlocale(locale.LC_ALL, "%s.UTF-8"%options.locale)
    reload(sys)
    sys.setdefaultencoding('utf-8')

    if not options.debug:
        if not setup_uid(options.user, options.group, options.log_file_prefix):
            logging.error("Cannot set UID/GID: %s/%s"%(options.user, options.group))
            sys.exit(1)

    logging.info("Starting %s webapp in a %s mode"%(options.domain, "debug" if options.debug else "production"))

    settings = dict(
        debug=options.debug,
        template_path=options.templates_path,
        autoescape=None,
    )

    http_server = tornado.httpserver.HTTPServer(tornado.web.Application(urls, **settings), xheaders=True)
    http_server.listen(options.bind_port, options.bind_host)
    logging.info("Server version %s binded to %s:%d"%(__version__, options.bind_host, options.bind_port))

    logging.info("Starting I/O loop to serve requests...")
    tornado.ioloop.IOLoop.instance().start()
