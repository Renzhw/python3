#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import re

picurl = "http://g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i1/1663105024352265720/TB2Nxguid0opuFjSZFxXXaDNVXa_!!0-saturn_solar.jpg"
root = "./pic/"
path = root+picurl.split('/')[-1]



def LoadPic():
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
	LoadPic()
	
main()