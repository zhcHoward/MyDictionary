#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base import DictionaryBase, WordNotFound


class Renren(DictionaryBase):
    """API for 人人词典"""
    _url = 'http://www.91dict.com/words?w={}'

    def parse_explanation(self):
        properties = self.soup.find(class_='tmInfo').find(class_='listBox')

        prop_strings = [p.strip() for p in properties.strings]

        # check if word found or not
        word_found = False
        for string in prop_strings:
            if string:
                word_found = True
                break
        if not word_found:
            raise WordNotFound(self.word)

        for p in prop_strings:
            if p:
                prop, explaination = p.split('.')
                self.result['explanation'][prop + '.'] = explaination.strip()

    def parse_pronunciation(self):
        for s in self.soup.find(class_='vos').stripped_strings:
            self.result['pronunciation'].append(' '.join((s[0], s[1:])))
