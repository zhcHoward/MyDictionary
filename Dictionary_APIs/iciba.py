#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4

from .base import DictionaryBase


class Iciba(DictionaryBase):
    """API for www.iciba.com"""
    _url = 'http://www.iciba.com/'

    def get_content(self):
        response = requests.get(self._url + self.word)
        return response.text

    def parse_content(self, content):
        soup = bs4.BeautifulSoup(content, 'html5lib')
        word = soup.find('h1', 'keyword').text
        properties = soup.find(class_='base-list').find_all(class_='clearfix')

        self.result = {}
        for each_prop in properties:
            prop = each_prop.find('span', 'prop').text
            explaination = each_prop.find('p').text.split()
            self.result[prop] = explaination

    def search(self, word=''):
        if not self.word or not word:
            self.result['error'] = ['No Word to Search']
        if word:
            self.word = word
        html = self.get_content()
        self.parse_content(html)

    def display(self):
        print(self.word)
        max_len = 0
        for key in self.result.keys():
            length = len(key)
            if length > max_len:
                max_len = length
        for prop, detail in self.result.items():
            prop_str = '{0:>{1}s}  '.format(prop, max_len)
            print(prop_str, end='')
            for d in detail:
                print(d + ' ', end='')
            print()
