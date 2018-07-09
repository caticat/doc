# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 其他的html解析库
# lxml:c语言编写的底层,速度很快
# HTML parser:python的内置模块,无需额外安装
