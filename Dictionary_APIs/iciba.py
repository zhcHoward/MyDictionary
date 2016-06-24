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
        properties = soup.find(class_='base-list').find_all(class_='clearfix')  # TODO error handling when word not found

        self.result = {}
        for each_prop in properties:
            prop = each_prop.find('span', 'prop').text
            explaination = each_prop.find('p').text.split()
            self.result[prop] = explaination
