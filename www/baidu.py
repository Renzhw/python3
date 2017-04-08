# -*- coding: utf-8 -*-
import sys, urllib, urllib.request, json

url = 'http://apis.baidu.com/apistore/dhc/getalltemplate?user=7f6254b8f81f84709228d6d419d488ac'


req = urllib.request.Request(url)

req.add_header("apikey", "3c32dcd5d7aabb56369075ceca2d748d")

resp = urllib.request.urlopen(req)
content = resp.read()
if(content):
    print(content)