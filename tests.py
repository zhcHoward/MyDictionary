#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nose.tools import raises

from dictionary import DictionaryAPI
from Dictionary_APIs import base, iciba, youdao


# iciba tests start
def test_iciba_english_to_chinese():
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


def test_iciba_chinese_to_english():
    expected_result = {
        'explanation': [('动', '（写字；记录；书写）write；'),
                        ('名', 'styleofcalligraphy；script；book；letter')],
        'pronunciation': ['[shū]']
    }
    dic = DictionaryAPI('书', service=iciba.Iciba)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


def test_iciba_english_phrase_to_chinese():
    expected_result = {'explanation': [('', '纠删码')], 'pronunciation': []}
    dic = DictionaryAPI('Erasure Code', service=iciba.Iciba)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


@raises(base.WordNotFound)
def test_iciba_word_not_found():
    dic = DictionaryAPI('ASDASDEWASD', service=iciba.Iciba)
    dic.service.get_content()
# iciba tests end


# youdao tests start
def test_youdao_english_to_chinese():
    expected_result = {
        'explanation': [
            ('n.', '书籍；卷；帐簿；名册；工作簿'),
            ('vt.', '预订；登记'),
            ('n.', '(Book)人名；(中)卜(广东话·威妥玛)；(朝)北；(英)布克；(瑞典)博克')
        ],
        'pronunciation': ['英 [bʊk]', '美 [bʊk]']
    }
    dic = DictionaryAPI('book', service=youdao.Youdao)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


def test_youdao_chinese_to_english():
    expected_result = {
        'explanation': [('n.', 'book; letter; script'), ('vt.', 'write')],
        'pronunciation': ['[shū]']
    }
    dic = DictionaryAPI('书', service=youdao.Youdao)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


def test_youdao_english_phrase_to_chinese():
    expected_result = {'explanation': [('', '纠删码')], 'pronunciation': []}
    dic = DictionaryAPI('Erasure Code', service=youdao.Youdao)
    dic.search()
    real_result = dic.service.result

    assert real_result == expected_result


@raises(base.WordNotFound)
def test_youdao_word_not_found():
    dic = DictionaryAPI('ASDASDEWASD', service=youdao.Youdao)
    dic.service.parse_content(dic.service.get_content())
    dic.service.parse_explanation()
# youdao tests end
