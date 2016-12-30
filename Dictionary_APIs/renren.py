#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4

from .base import DictionaryBase


class Renren(DictionaryBase):
    """API for 人人词典"""
    _url = 'http://www.91dict.com/'

    def get_content(self):
        response = requests.get(self._url + 'words?w=' + self.word)
        return response.text

    def parse_content(self, content):
        soup = bs4.BeautifulSoup(content, 'html5lib')
        properties = soup.find(class_='tmInfo').find(class_='listBox')

        self.result = {}
        prop_strings = [p.strip() for p in properties.strings]
        for p in prop_strings:
            if p:
                prop, explaination = p.split('.')
                self.result[prop+'.'] = explaination.strip()

    def display(self):
        max_len = 0
        for key in self.result.keys():
            length = len(key)
            if length > max_len:
                max_len = length
        for prop, detail in self.result.items():
            prop_str = '{0:>{1}s} '.format(prop, max_len)
            print(prop_str + detail)

