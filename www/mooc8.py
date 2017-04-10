#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#jiandan-meizitu,并保存至本地
import requests
import os
import re

a = 2426
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
    return[a+str(i) for i in lst]

def LoadPic(picurl,path):
	try:
		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(path):
			r = requests.get(picurl)
			with open(path,'wb') as f:
				f.write(r.content)
				f.close()
				print("文件保存成功")
		else:
				print("文件已保存")
	except:
		print("爬取失败")

def main():
	infoList = []
	rex = r'href="//w[xw][1-4].sinaimg.cn/large.*?.[jpg,png,gif]"'
	plt = re.findall(rex,getHTMLText(url))
	for i in range(len(plt)):
		picurl = eval(plt[i].split('=')[1])
		infoList.append(picurl)
	picfile = foo(infoList,'http:')
	for i in picfile:
		path = root+url.split('page-')[1]+i.split('/')[-1]
		LoadPic(i,path)

while a >= 2420:
    print(a)
    b=str(a)
    root = "./pic/"+b+"/"
    url = 'http://jandan.net/ooxx/page-'+str(a)
    main()
    a=a-1





