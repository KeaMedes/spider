# -*- coding: utf-8 -*-
from time import time


class Task(object):
    def __init__(self, url, parser, **kwargs):
        self.parser = parser
        self.delay = 0
        self.create_time = int(round(time() * 1000))
        self.socks5_proxy = ''
        self.http_proxy = ''
        self.https_proxy = ''
        self.priority = 0

        if 'delay' in kwargs:
            self.delay = int(kwargs['delay'])

        if 'socks5_proxy' in kwargs:
            self.socks5_proxy = kwargs['socks5_proxy']

        if 'http_proxy' in kwargs:
            self.http_proxy = kwargs['http_proxy']

        if 'https_proxy' in kwargs:
            self.https_proxy = kwargs['https_proxy']

        if 'priority' in kwargs:
            self.priority = int(kwargs['priority'])

        self.use_proxy = self.socks5_proxy or self.http_proxy or self.https_proxy
        from urlparse import urlparse
        self.url = urlparse(url)

    def response(self):
        pass
