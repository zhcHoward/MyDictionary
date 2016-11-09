#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DictionaryBase(object):
    """Base API for all other APIs"""
    _url = ''

    def __init__(self, word=''):
        self.word = word
        self.result = {}

    def get_content(self):
        pass

    def parse_content(self, content):
        pass

    def search(self, word=''):
        if not self.word or not word:
            self.result['error'] = ['No Word to Search']
        if word:
            self.word = word
        html = self.get_content()
        self.parse_content(html)

    def display(self):
        max_len = 0
        for key in self.result.keys():
            length = len(key)
            if length > max_len:
                max_len = length
        for prop, detail in self.result.items():
            prop_str = '{0:>{1}s} '.format(prop, max_len)
            print(prop_str, end='')
            for d in detail:
                print(d + ' ', end='')
            print()
