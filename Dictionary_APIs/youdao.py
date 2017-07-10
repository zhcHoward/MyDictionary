#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base import DictionaryBase, WordNotFound


class Youdao(DictionaryBase):
    """API for 有道词典"""
    _url = 'http://www.youdao.com/w/{}/'

    def parse_explanation(self):
        try:
            translation_list = self.soup.find(class_='trans-container').find_all('li')
        except AttributeError:
            raise WordNotFound(self.word)

        for trans in translation_list:
            prop, explanation = trans.text.split(maxsplit=1)
            self.result['explanation'][prop] = explanation

    def parse_pronunciation(self):
        spans = self.soup.find_all(class_='pronounce')
        self.result['pronunciation'] = [' '.join(span.stripped_strings) for span in spans]