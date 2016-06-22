#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Dictionary_APIs.iciba import Iciba


class DictionaryAPI(object):
    """docstring for DictionaryAPI"""

    def __init__(self, word='', service=Iciba):
        self.service = service(word)

    def search(self, word):
        self.service.search(word)

    def display(self):
        self.service.display()


if __name__ == '__main__':
    dictionary = DictionaryAPI('place')
    dictionary.search('work')
    dictionary.display()
