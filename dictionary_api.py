#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from iciba import Iciba


class DictionaryAPI(object):
    """docstring for DictionaryAPI"""

    def __init__(self, service=Iciba):
        self.service = service

    def search(self, word)
