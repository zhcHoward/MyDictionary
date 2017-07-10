#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class DictionaryBase():
    """Base Dictionary API for all other APIs"""
    _url = '{}'

    def __init__(self, word=''):
        # store the word will be searched
        self.word = word
        # store explanation in the format {prop: meaning}
        self.result = {
            'explanation': {},
            'pronunciation': [],
        }
        # store BeautifulSoup object
        self.soup = None

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
        """main function for search word"""
        html = self.get_content()
        try:
            self.parse_content(html)
            self.parse_explanation()
            self.parse_pronunciation()
        except WordNotFound as e:
            print(e)

    @property
    def max_prop_length(self):
        """by finding the max length of prop, to format the output for displaying"""
        return max([len(prop) for prop in self.result['explanation']])

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
        print(', '.join([p for p in self.result['pronunciation']]))

        for prop, detail in self.result['explanation'].items():
            prop_str = '{0:>{1}s} '.format(prop, self.max_prop_length)
            print(prop_str + detail)


class WordNotFound(Exception):
    "Exception raised when word not found"
    def __init__(self, word):
        self.msg = 'Word "{}" not found'.format(word)

