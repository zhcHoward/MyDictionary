#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4


url = 'http://www.iciba.com/'
word = input('Please input a word: ')

response = requests.get(url + word)
html = response.text
soup = bs4.BeautifulSoup(html, 'html5lib')

word = soup.find('h1', 'keyword').text
explains_html = soup.find_all(attrs={'class': 'base-list'})
explains = []
for each_prop in explains_html.find_all(attrs={'class': 'clearfix'}):
    explains.append({
        each_prop.find('span', 'prop').text: each_prop.find('p').split()
    })
