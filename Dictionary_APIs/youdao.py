#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
import re

from .base import DictionaryBase, WordNotFound


class Youdao(DictionaryBase):
    _url = 'http://www.youdao.com/w/{}/'

    def parse_content(self, content):
        soup = bs4.BeautifulSoup(content, 'html5lib')

        try:
            translation_list = soup.find(class_='trans-container').find_all('li')
        except AttributeError:
            raise WordNotFound

        for trans in translation_list:
            pattern = re.compile(r'^(\w+\.)\s(.*?)$')
            r = pattern.match(trans.text)
            self.result[r.group(1)] = r.group(2)
