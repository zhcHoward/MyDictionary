#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class DictionaryBase(object):
    """Base Dictionary API for all other APIs"""
    _url = '{}'

    def __init__(self, word=''):
        # store the word will be searched
        self.word = word
        # store explaination in the format {prop: meaning}
        self.result = {}

    def get_content(self):
        """get pure html from website"""
        response = requests.get(self._url.format(self.word))
        return response.text

    def parse_content(self, content):
        """get useful info out of the whole html"""
        raise NotImplementedError('parse_content function need to be implemented')

    def search(self):
        """main function for search word"""
        html = self.get_content()
        try:
            self.parse_content(html)
        except WordNotFound:
            print('Word "{}" not found'.format(self.word))

    @property
    def max_prop_length(self):
        """"""
        max_len = 0
        for key in self.result.keys():
            length = len(key)
            if length > max_len:
                max_len = length
        return max_len

    def display(self):
        """format self.result for displaying"""
        max_len = self.max_prop_length
        for prop, detail in self.result.items():
            prop_str = '{0:>{1}s} '.format(prop, max_len)
            print(prop_str + detail)


class WordNotFound(Exception):
    pass
