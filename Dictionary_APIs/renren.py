#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4

from .base import DictionaryBase, WordNotFound


class Renren(DictionaryBase):
    """API for 人人词典"""
    _url = 'http://www.91dict.com/words?w={}'

    def parse_content(self, content):
        soup = bs4.BeautifulSoup(content, 'html5lib')
        properties = soup.find(class_='tmInfo').find(class_='listBox')

        prop_strings = [p.strip() for p in properties.strings]

        # check if word found or not
        word_found = False
        for string in prop_strings:
            if string:
                word_found = True
                break
        if not word_found:
            raise WordNotFound

        for p in prop_strings:
            if p:
                prop, explaination = p.split('.')
                self.result[prop+'.'] = explaination.strip()
