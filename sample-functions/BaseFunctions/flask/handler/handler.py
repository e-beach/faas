#!/usr/bin/python
from wsgiref.handlers import CGIHandler
import os
from app import app
import urllib.parse as urlparse

url = "http://localhost:8080%s%s" % (os.getenv("Http_Path", default="/hello"), os.getenv("Http_Query", default=""))
query_params = urlparse.urlsplit(url).query
dict_query_params = dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
whole_path = urlparse.urlparse(url).path
split_path = whole_path.split('/')
route_path = split_path[(len(split_path)-1)]


class ProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SERVER_NAME'] = "localhost"
        environ['SERVER_PORT'] = "8080"
        environ['REQUEST_METHOD'] = "GET"
        environ['SCRIPT_NAME'] = ""
        environ['PATH_INFO'] = "/%s" % route_path
        environ['QUERY_STRING'] = query_params
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        return self.app(environ, start_response)

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)

