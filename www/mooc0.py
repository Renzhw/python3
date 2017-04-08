#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
url = "http://img10.360buyimg.com/imgzone/jfs/t4420/293/228122876/59076/76a199cb/58cbd0fdN047bcdb8.jpg"
root = "./www/"
path = root+url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
			print("文件已保存")
except:
	print("爬取失败")