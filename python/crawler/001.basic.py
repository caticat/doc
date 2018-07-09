# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__=='__main__':
	html = urlopen("http://www.pythonscraping.com/pages/page1.html")
	bsObj = BeautifulSoup(html.read(), "html.parser")
	print(bsObj.html.body.h1)
	print(bsObj.html.h1)
	print(bsObj.body.h1)
	print(bsObj.h1)
