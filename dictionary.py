#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

from Dictionary_APIs.iciba import Iciba
from Dictionary_APIs.youdao import Youdao


dictionaries = {
    'iciba': Iciba,
    'youdao': Youdao,
}


class DictionaryAPI(object):
    """docstring for DictionaryAPI"""

    def __init__(self, word='', service=Iciba):
        with open('config.json') as file:
            configs = json.load(file)
        default_dictionary = configs.get('default_dictionary', None)
        if default_dictionary:
            self.service = dictionaries[default_dictionary](word)
        else:
            self.service = service(word)

    def search(self, word=''):
        if word:
            self.service.search(word)
        else:
            self.service.search()

    def display(self):
        self.service.display()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        kwargs = {
            'word': sys.argv[1],
            'service': dictionaries.get(sys.argv[2])
        }
    else:
        kwargs = {
            'word': sys.argv[1],
        }
    dictionary = DictionaryAPI(**kwargs)
    dictionary.search()
    dictionary.display()
