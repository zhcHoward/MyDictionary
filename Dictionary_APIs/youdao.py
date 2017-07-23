#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from .base import DictionaryBase, WordNotFound


class Youdao(DictionaryBase):
    """API for 有道词典"""
    _url = 'http://www.youdao.com/w/{}/'

    def parse_content(self, content):
        self.soup = BeautifulSoup(content, 'html5lib').find(id='results-contents')
        if self.soup.find(class_='error-wrapper'):
            raise WordNotFound(self.word)

    def parse_explanation(self):
        trans_container = self.soup.find(class_='trans-container')
        if not trans_container:
            raise WordNotFound(self.word)

        translation_list = trans_container.find_all('li')
        if translation_list:
            for trans in translation_list:
                try:
                    prop, explanation = trans.text.split(maxsplit=1)
                except ValueError:
                    prop, explanation = '', trans.text
                self.result['explanation'].append((prop, explanation))
        else:
            translation_list = trans_container.find_all(class_='wordGroup')
            for trans in translation_list:
                prop = trans.span.text
                explanation = [''.join(t.stripped_strings) for t in trans.find_all(class_='contentTitle')]
                self.result['explanation'].append((prop, ' '.join(explanation)))

    def parse_pronunciation(self):
        spans = self.soup.find_all(class_='pronounce')
        if spans:
            self.result['pronunciation'] = [
                ' '.join(s.stripped_strings) for s in spans if list(s.stripped_strings)
            ]
        else:
            self.result['pronunciation'] = [self.soup.find(class_='phonetic').text]
