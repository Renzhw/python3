#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import re

def foo(lst,a):
    return[a+str(i) for i in lst]
lst = ['www.baidu.com','www.baidu.com','www.baidu.com','www.baidu.com','www.baidu.com']
a = 'http://'
b = []
b.append((foo(lst,a)))
c = foo(lst,a)
print(c[1])
print(lst)