#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class DictionaryBase():
    """Base Dictionary API for all other APIs"""
    _url = '{}'

    def __init__(self, word=''):
        self.word = word    # word to be searched
        self.result = {
            'explanation': [],  # e.g. [('n.', '书；卷；课本；账簿'), ('vt.& vi.', '预订；'), ...]
            'pronunciation': [],
        }
        # store BeautifulSoup object
        self.soup = None
        self.max_prop_length = 0

    def get_max_prop_length(self):
        """by finding the max length of prop, to format the output for displaying"""
        self.max_prop_length = max([len(prop) for prop, explanation in self.result['explanation']])

    def get_content(self):
        """get pure html from website"""
        response = requests.get(self._url.format(self.word))
        return response.text

    def parse_content(self, content):
        """get useful info out of the whole html"""
        self.soup = BeautifulSoup(content, 'html5lib')

    def parse_pronunciation(self):
        raise NotImplementedError('parse_pronunciation function need to be implemented')

    def parse_explanation(self):
        raise NotImplementedError('parse_explanation function need to be implemented')

    def search(self):
        """main function for search a word"""
        try:
            html = self.get_content()
            self.parse_content(html)
            self.parse_explanation()
            self.parse_pronunciation()
            self.get_max_prop_length()
        except WordNotFound as e:
            print(e)

    def display(self):
        """format self.result for displaying
        example output:
        dictionary book
        英 [bʊk], 美 [bʊk]
              n. 书；卷；课本；账簿
        vt.& vi. 预订；
             vt. 登记；（向旅馆、饭店、戏院等）预约；立案（控告某人）；订立演出契约
            adj. 书的；账簿上的；得之（或来自）书本的；按照（或依据）书本的
        """
        if self.result['pronunciation']:
            print(', '.join([p for p in self.result['pronunciation']]))

        for prop, explanation in self.result['explanation']:
            prop_str = '{0:>{1}s} '.format(prop, self.max_prop_length)
            print(prop_str + explanation)


class WordNotFound(Exception):
    "Exception raised when word not found"
    def __init__(self, word):
        self.msg = 'Word "{}" not found'.format(word)

    def __str__(self):
        return self.msg

