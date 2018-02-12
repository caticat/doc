# -*- coding:utf-8 -*-

# 插入排序
# 时间复杂度:O(n^2)
# 稳定排序

def sortInsert(argv):
	l = len(argv)
	for i in range(1, l):
		x = argv[i]
		j = i - 1
		while j >= 0 and x < argv[j]:
			argv[j + 1] = argv[j]
			j -= 1
		argv[j + 1] = x

if __name__ == "__main__":
	a = [3,1,5,7,2,4,9,6]
	sortInsert(a)
	print(a)
