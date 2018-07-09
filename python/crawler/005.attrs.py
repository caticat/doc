# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 直接使用对象的属性和调用`attrs`后获取dict的属性其实是一样的

if __name__=='__main__':
	html = urlopen("http://www.pythonscraping.com/pages/page3.html")
	bsObj = BeautifulSoup(html.read(), "html.parser")
	images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
	for image in images:
		print(image) # 标签对象
		print(image.attrs) # 标签的属性字典
		print(image["src"]) # 属性值
		print(image.attrs["src"]) # 属性值
