#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import cookielib
import urllib2
import csv
from bs4 import BeautifulSoup


def getSetUrl(setNum, lang):
    setUrl = 'https://scryfall.com/sets'
    setUrl = setUrl + '/' + setNum
    if lang:
        setUrl = setUrl + '/' + lang
    return setUrl


def getResponse(url):
    response = urllib2.urlopen(url)
    return (response.getcode(), response.read())


def downloadImage(imgUrl, path):
    conn = urllib2.urlopen(imgUrl)
    with open(path, 'wb') as f:
        f.write(conn.read())


def getImages(dirPath, html):
    if not os.path.exists(dirPath):
        print(dirPath)
        os.makedirs(dirPath)
    csvfile = file(dirPath + '/summary.csv', 'wb')
    writer = csv.writer(csvfile)

    baseImageUrl = 'https://img.scryfall.com/cards/normal/front'
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    a_nodes = soup.find_all('a', class_='card-grid-item-card')
    total = len(a_nodes)
    i = 0
    for a in a_nodes:
        i = i + 1
        id = a.parent['data-card-id']
        title = a.img['title']
        src = baseImageUrl + '/' + id[0] + '/' + id[1] + '/' + id + '.jpg'
        name = a.span.text
        writer.writerow([id, title, name])
        downloadImage(src, dirPath + '/' + id + '.jpg')
        log('downloaded: [%d/%d] %s (%s)' % (i, total, title, name))
    csvfile.close()


def log(message):
    print(message)


def run(setNum, lang, dirPath):
    requestUrl = getSetUrl(setNum, lang)
    (status, html) = getResponse(requestUrl)
    if status == 200:
        getImages(dirPath, html)
    else:
        log('Http error: %d' % status)


if __name__ == '__main__':
    run('grn', 'zhs', 'Guilds of Ravnica (GRN)')
