#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nose.tools import raises

from dictionary import DictionaryAPI
from Dictionary_APIs import base, iciba


def test_english_to_chinese():
    expected_result = {
        'explanation': [
            ('n.', '书；卷；课本；账簿'),
            ('vt.& vi.', '预订；'),
            ('vt.', '登记；（向旅馆、饭店、戏院等）预约；立案（控告某人）；订立演出契约'),
            ('adj.', '书的；账簿上的；得之（或来自）书本的；按照（或依据）书本的')
        ],
        'pronunciation': ['英 [bʊk]', '美 [bʊk]']
    }
    dic = DictionaryAPI('book', service=iciba.Iciba)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


def test_chinese_to_english():
    expected_result = {
        'explanation': [('动', '（写字；记录；书写）write；'),
                        ('名', 'styleofcalligraphy；script；book；letter')],
        'pronunciation': ['[shū]']
    }
    dic = DictionaryAPI('书', service=iciba.Iciba)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


def test_english_phrase_to_chinese():
    expected_result = {'explanation': [('', '纠删码')], 'pronunciation': []}
    dic = DictionaryAPI('Erasure Code', service=iciba.Iciba)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


@raises(base.WordNotFound)
def test_word_not_found():
    dic = DictionaryAPI('ASDASDEWASD', service=iciba.Iciba)
    dic.service.get_content()
