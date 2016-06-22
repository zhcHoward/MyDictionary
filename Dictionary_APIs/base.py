#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class DictionaryBase(object):
    """Base API for all other APIs"""
    _url = ''

    def __init__(self, word=''):
        self.word = word
        self.result = {}

    def get_content(self):
        pass

    def parse_content(self, content):
        pass

    def search(self, word=''):
        pass

    def display(self):
        pass
