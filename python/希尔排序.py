# -*- coding:utf-8 -*-

# 希尔排序
# 时间复杂度:<O(n^2)
# 直接插入排序的优化算法
# 不稳定排序
# 希尔排序是基于插入排序的以下两点性质而提出改进方法的：
# 1. 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率。
# 2. 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。

def sortShell(argv, div = None):
	l = len(argv)
	if div == None:
		div = l // 2
	if div == 0:
		return
	for i in range(div, l):
		x = argv[i]
		j = i - div
		while j >= 0 and x < argv[j]:
			argv[j + div] = argv[j]
			j -= div
		argv[j + div] = x
	sortShell(argv, div // 2)

if __name__ == "__main__":
	a = [3, 1, 5, 7, 2, 4, 9, 6]
	sortShell(a, 1) # 当div直接设置为1时,希尔排序就是直接插入排序
	print(a)
	sortShell(a)
	print(a)
