# -*- coding:utf-8 -*-

# 堆排序
# 时间复杂度:<O(nlogn)
# 稳定排序
# 思路:
# 	1. 将数组转化成有序堆
# 	2. 每次将堆顶元素取出放入有序列表中
# 	3. 重新转化有序堆
# 	4. 重复步骤2,3直至排序完毕

# 调整堆的指定位置的内容(这里是大顶堆(就是大的元素为根))
def heapAdjust(argv, idx, l):
	child = 2 * idx + 1
	while (child < l):
		if (child + 1 < l) and (argv[child] < argv[child + 1]):
			child += 1
		if argv[idx] < argv[child]:
			argv[idx], argv[child] = argv[child], argv[idx]
			idx = child
			child = 2 * idx + 1
		else:
			break

# 创建堆
def heapBuild(argv):
	l = len(argv)
	for i in range((l - 1)//2, -1, -1):
		heapAdjust(argv, i, l)

# 堆排序
def sortHeap(argv):
	l = len(argv)
	heapBuild(argv)
	for i in range(l - 1, 0, -1):
		argv[0], argv[i] = argv[i], argv[0]
		heapAdjust(argv, 0, i)

if __name__ == "__main__":
	a = [3, 1, 5, 7, 2, 4, 9, 6]
	sortHeap(a)
	print(a)
