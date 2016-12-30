#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from os.path import dirname, abspath, join

from Dictionary_APIs import *


dictionaries = {
    'iciba': iciba.Iciba,
    'youdao': youdao.Youdao,
    'renren': renren.Renren,
}


class DictionaryAPI(object):
    def __init__(self, word='', service=dictionaries['iciba']):
        self.service = service(word)

    def search(self, word=''):
        if word:
            self.service.search(word)
        else:
            self.service.search()

    def display(self):
        self.service.display()


if __name__ == '__main__':
    base_dir = dirname(abspath(__file__))
    with open(join(base_dir, 'config.json')) as file:
        configs = json.load(file)
    default_dictionary = configs.get('default_dictionary', None)
    service = {}
    if default_dictionary:
        service['service'] = dictionaries[default_dictionary]

    if len(sys.argv) == 3:
        kwargs = {
            'word': sys.argv[1],
            'service': dictionaries.get(sys.argv[2])
        }
    else:
        kwargs = {
            'word': sys.argv[1],
        }
        kwargs.update(service)

    dictionary = DictionaryAPI(**kwargs)
    dictionary.search()
    dictionary.display()

