# -*- coding:utf-8 -*-

# 插入排序
# 时间复杂度:O(n^2)
# 稳定排序
# 思路:
# 	1. 从索引1开始,顺序遍历
#	2. 每个元素都和前面的元素倒叙做比较
# 		1. 如果大于前面的元素则插入其中
#		2. 如果小于前面的元素则重复和再上一个元素做比较
#	3. 遍历结束后即可完成排序

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
