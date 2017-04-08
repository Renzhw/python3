#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#jiandan-meizitu,并保存链接地址到本地txt文件中
import requests
import os
import re

a = 2240
print('开始爬取煎蛋网美女图片')
allpicurl=[]
def getHTMLText(url):
	try:
		headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
		r = requests.get(url, timeout=30,headers=headers)
		r.raise_for_status()
		return r.text
	except:
		return ""

def foo(lst,a):
    return(a+lst)

def main():
	infoList = []
	rex = r'href="//w[wx][0-9].sinaimg.cn/large.*?.[jpg,png,gif]"'
	plt = re.findall(rex,getHTMLText(url))
	for i in range(len(plt)):
		picurl = eval(plt[i].split('=')[1])
		picurl = foo(picurl,'http:')
		file.write(str(picurl)+"\n")
file=open('data.txt','a')	
while a >= 0:
    print(a)
    b=str(a)
    root = "./pic/"+b+"/"
    url = 'http://jandan.net/ooxx/page-'+str(a)
    main()
    a=a-1
file.close()


