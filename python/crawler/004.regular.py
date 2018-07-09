# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 正则表达式的使用

if __name__=='__main__':
	html = urlopen("http://www.pythonscraping.com/pages/page3.html")
	bsObj = BeautifulSoup(html.read(), "html.parser")
	images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
	for image in images:
		print(image["src"])
