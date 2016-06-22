#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from Dictionary_APIs.iciba import Iciba
from Dictionary_APIs.youdao import Youdao


class DictionaryAPI(object):
    """docstring for DictionaryAPI"""

    def __init__(self, word='', service=Youdao):
        self.service = service(word)

    def search(self, word):
        self.service.search(word)

    def display(self):
        self.service.display()


if __name__ == '__main__':
    word = sys.argv[1]
    dictionary = DictionaryAPI()
    dictionary.search(word)
    dictionary.display()
