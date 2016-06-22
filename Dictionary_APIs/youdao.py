#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4
import re

from .base import DictionaryBase


class Youdao(DictionaryBase):
    _url = 'http://www.youdao.com/w/{}/'

    def get_content(self):
        response = requests.get(self._url.format(self.word))
        return response.text

    def parse_content(self, content):
        soup = bs4.BeautifulSoup(content, 'html5lib')
        translation_list = soup.find(class_='trans-container').find_all('li')

        self.result = {}
        for trans in translation_list:
            pattern = re.compile(r'^(\w+\.)\s(.*?)$')
            r = pattern.match(trans.text)
            self.result[r.group(1)] = r.group(2)

    def display(self):
        max_len = 0
        for key in self.result.keys():
            length = len(key)
            if length > max_len:
                max_len = length
        for prop, detail in self.result.items():
            prop_str = '{0:>{1}s} '.format(prop, max_len)
            print(prop_str + detail)