# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 过滤查找到的内容

if __name__=='__main__':
	html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
	bsObj = BeautifulSoup(html, "html.parser")

	# 基本的连接查找,但是还有很多多余的内容
	links = bsObj.findAll("a")
	for link in links:
		if "href" in link.attrs:
			print(link.attrs["href"])

	print("_______________________________________")

	# 过滤掉所有不关注的内容
	# r''是表示不转义后面的字符串
	# `?!`是不包含的意思
	links = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile(r'^/wiki/((?!:).)*$'))
	for link in links:
		print(link.attrs["href"])
