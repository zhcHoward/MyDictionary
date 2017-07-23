#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from .base import DictionaryBase, WordNotFound


class Iciba(DictionaryBase):
    """API for 爱词霸"""
    _url = 'http://www.iciba.com/{}'
    # url 也可以用'http://dict-co.iciba.com/search.php?word={}&submit=查询'
    # 但是用这个url返回的结果对中英查询不太友好

    def get_content(self):
        response = requests.get(self._url.format(self.word), allow_redirects=False)
        if response.status_code == 302:
            raise WordNotFound(self.word)
        return response.text

    def parse_content(self, content):
        self.soup = BeautifulSoup(content, 'html5lib').find(class_='in-base')

    def parse_explanation(self):
        base_list = self.soup.find(class_='base-list')
        if base_list:
            # English ==> Chinese
            properties = base_list.find_all(class_='clearfix')
            for each_prop in properties:
                prop = each_prop.find('span', 'prop').text
                explanation = ''.join(each_prop.find('p').text.split())
                self.result['explanation'].append((prop, explanation))
        else:
            # Chinese ==> English and some special phrase e.g. "Erasure Code"
            explanation = self.soup.find(class_='in-base-top').div.text
            self.result['explanation'].append(('', explanation))

    def parse_pronunciation(self):
        try:
            pronunciation_div = self.soup.find(class_='base-speak')
            self.result['pronunciation'] = list(pronunciation_div.stripped_strings)
        except AttributeError:
            pass  # if word has no phonetic symbol, do nothing
