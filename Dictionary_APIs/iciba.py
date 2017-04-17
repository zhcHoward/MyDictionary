#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4

from .base import DictionaryBase, WordNotFound


class Iciba(DictionaryBase):
    """API for 爱词霸"""
    _url = 'http://www.iciba.com/{}'

    def parse_content(self, content):
        soup = bs4.BeautifulSoup(content, 'html5lib')

        try:
            properties = soup.find(class_='base-list').find_all(class_='clearfix')
        except AttributeError:
            raise WordNotFound

        for each_prop in properties:
            prop = each_prop.find('span', 'prop').text
            explaination = each_prop.find('p').text.split()
            self.result[prop] = ''.join(explaination)
