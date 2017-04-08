#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import re
import random
print('请输入爬取关键字')
url = 'https://s.taobao.com/search?q=' + input()   
print('页面深度为1')
depth = 1
root = "./pic/"
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
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
	picfile = []
	for i in range(depth):
		plt = re.findall(r'\"pic_url\"\:\".*?\"',getHTMLText(url))
	for i in range(len(plt)):
		picurl = eval(plt[i].split(':')[1])
		infoList.append(picurl)
	picfile = foo(infoList,'https:')
	for i in picfile:
		path = root+i.split('/')[-1]
		LoadPic(i,path)
main()



