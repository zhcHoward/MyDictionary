#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import requests
import bs4

if __name__ == '__main__':
    url = 'http://www.iciba.com/'
    word = sys.argv[1]

    response = requests.get(url + word)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html5lib')

    word = soup.find('h1', 'keyword').text
    explains_html = soup.find(attrs={'class': 'base-list'})
    explains = {}
    for each_prop in explains_html.find_all(attrs={'class': 'clearfix'}):
        # result = each_prop.find(attrs={'class': 'clearfix'})
        explains.update({
            each_prop.find('span', 'prop').text: each_prop.find('p').text.split()
        })

    print(word + ':')
    for prop, detail in explains.items():
        print(prop + '\t', end='')
        for d in detail:
            print(d + ' ', end='')
        print()
