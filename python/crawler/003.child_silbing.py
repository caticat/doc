# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 不直接使用`bsObj.table.xxx`的原因是不能保证下次table还是在第一个位置,保证代码更稳定

if __name__=='__main__':
	html = urlopen("http://www.pythonscraping.com/pages/page3.html")
	bsObj = BeautifulSoup(html.read(), "html.parser")
	for child in bsObj.find("table", {"id":"giftList"}).children: # 子标签
		print(child)
	print("_______________")
	for child in bsObj.find("table", {"id":"giftList"}).descendants: # 后代标签(子标签+子子标签+...)
		print(child)
	print("_______________")
	for silbing in bsObj.find("table", {"id":"giftList"}).tr.next_siblings: # 获取同级的其他数据
		print(silbing)
	print("_______________")
	print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
