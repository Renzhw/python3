#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#CrowTaobaoPrice.py
import requests
import re
import os
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        dlt = re.findall(r'\"pic_url\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            dizhi = eval(dlt[i].split(':')[1])
            ilt.append([price , dizhi])
    except:
        print("")
 
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:32}"
    print(tplt.format("序号", "价格", "地址"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 1
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()