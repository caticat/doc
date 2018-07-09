# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# findAll函数可以使用lambda表达式来过滤查找的内容

if __name__=='__main__':
	html = urlopen("http://www.pythonscraping.com/pages/page3.html")
	bsObj = BeautifulSoup(html.read(), "html.parser")
	# tags = bsObj.findAll(lambda tag: len(tag.attrs) == 1)
	tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
	for tag in tags:
		print(tag.name, tag.attrs) # 标签对象
		print("______________________")
