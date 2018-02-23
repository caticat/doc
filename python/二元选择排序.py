# -*- coding:utf-8 -*-

# 二元选择排序
# 时间复杂度:<O((n^2)/2)
# 不稳定排序(我的写法)
# 思路:
# 	同简单选择排序,不过同时排最大和最小值

def sortSimpleSelectionOpti(argv):
	l = len(argv)
	r = l // 2
	if l % 2:
		r += 1
	for i in range(1, r):
		b = i - 1
		e = l - i
		min = b
		max = e
		for j in range(b, e):
			if argv[min] > argv[j]:
				min = j
			if argv[max] < argv[j]:
				max = j
		argv[b], argv[min] = argv[min], argv[b]
		argv[e], argv[max] = argv[max], argv[e]

if __name__ == "__main__":
	a = [3, 1, 5, 7, 2, 4, 9, 6]
	sortSimpleSelectionOpti(a)
	print(a)
