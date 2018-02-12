# -*- coding:utf-8 -*-

# 简单选择排序
# 时间复杂度:<O(n^2)
# 稳定排序
# 思路:
# 	1. 遍历数组
# 	2. 每次选择数组中最小的一个放在前面
#	3. 选择次小的一个放在前一次排序的后面
#	4. 重复操作直到最后一个元素

def sortSimpleSelection(argv):
	l = len(argv)
	for i in range(1, l):
		idx = i - 1
		min = argv[idx]
		for j in range(i, l):
			if argv[j] < min:
				idx = j
				min = argv[idx]
		argv[i - 1], argv[idx] = argv[idx], argv[i - 1]

if __name__ == "__main__":
	a = [3, 1, 5, 7, 2, 4, 9, 6]
	sortSimpleSelection(a)
	print(a)
