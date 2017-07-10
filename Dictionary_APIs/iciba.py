#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base import DictionaryBase, WordNotFound


class Iciba(DictionaryBase):
    """API for 爱词霸"""
    _url = 'http://www.iciba.com/{}'
    # url 也可以用'http://dict-co.iciba.com/search.php?word={}&submit=查询'
    # 但是用这个url返回的结果对中英查询不太友好

    def parse_explanation(self):
        try:
            properties = self.soup.find(class_='base-list').find_all(class_='clearfix')
        except AttributeError:
            raise WordNotFound(self.word)

        for each_prop in properties:
            prop = each_prop.find('span', 'prop').text
            explanation = each_prop.find('p').text.split()
            self.result['explanation'][prop] = ''.join(explanation)

    def parse_pronunciation(self):
        pronunciation_div = self.soup.find(class_='base-speak')
        self.result['pronunciation'] = list(pronunciation_div.stripped_strings)
