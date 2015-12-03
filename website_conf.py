# -*- coding: utf-8 -*-
class WebSiteConf(object):
    def __init__(self):
        from os.path import isfile, dirname, join, abspath
        website_config_file = join(dirname(abspath(__file__)), 'website.json')
        if isfile(website_config_file):
            from json import load
            with open(website_config_file) as f:
                website_config = load(f)
        else:
            website_config = {}

        self._website_config_file = website_config_file
        self._website_config = website_config

    def prepare_exit(self):
        from json import dump
        with open(self._website_config_file) as f:
            dump(self._website_config, f)

    def interval(self, netloc):
        if netloc not in self._website_config:
            self._website_config[netloc] = {
                "interval": 100
            }
            return 100
        else:
            return self._website_config[netloc]

website_config = WebSiteConf()
