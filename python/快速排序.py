# -*- coding: utf-8 -*-

import math

def sort(orderedList):
    pass

def key(orderedList, value, begin = 0, end = -1):
    if end == -1:
        end = len(orderedList)
    if begin >= end:
        return begin
    length = end - begin
    if length <= 1:
        return begin
    index = int((begin + end) / 2)
    if orderedList[index] == value:
        return index
    elif orderedList[index] > value:
        end = index
    else:
        begin = index + 1
    return key(orderedList, value, begin, end)

def key1(orderedList, value):
    begin = 0
    end = len(orderedList)
    mid = int(end / 2)
    while ((end > begin) and (orderedList[mid] != value)):
        if (orderedList[mid] < value):
            begin = mid # + 1
        else:
            end = mid
        mid = int((begin + end) / 2)
    return mid

def test(orderedList, value):
    print("查找[%s]索引[%s][%s]" % (value, key(orderedList, value), key1(orderedList, value)))

def test2(orderedList, angle):
    radius = angleToRadius(angle)
    value = math.tan(radius)
    print("角度[%s]弧度[%.2f]值[%.2f]:[%s][%s]" % (angle, radius, value, key(orderedList, value), key1(orderedList, value)))

def angleToRadius(angle):
    return angle * math.pi / 180

def qtest(list):
    lc = list.copy()
    qsort(list)
    qsort_2(lc, 0, len(lc) - 1)
    print(list, lc)

def qsort(data, front = 0, back = 1, init = True):
    # 条件校验
    if front >= back:
        return

    # 初始化
    if init:
        back = len(data) - 1

    # 单步排序
    i = front
    j = back
    key = data[i]
    middle = i
    backward = True
    while i < j:
        if backward:
            if data[j] < key:
                data[i], data[j] = data[j], data[i]
                i += 1
                backward = False
                middle = j
            else:
                j -= 1
        else:
            if data[i] > key:
                data[i], data[j] = data[j], data[i]
                j -= 1
                backward = True
                middle = i
            else:
                i += 1

    # 递归
    qsort(data, front, middle - 1, False)
    qsort(data, middle + 1, back, False)

def qsort_2(data, low, high):
    if low >= high:
        return
    front = low
    back = high
    key = data[front]
    while front < back:
        while front < back and data[back] >= key:
            back -= 1
        data[front] = data[back]
        while front < back and data[front] <= key:
            front += 1
        data[back] = data[front]
    data[front] = key
    qsort_2(data, low, front - 1)
    qsort_2(data, front + 1, high)

if __name__ == "__main__":
    print("开始")

    qtest([6, 2, 7, 3, 8, 9])
    qtest([5, 4])
    qtest([6, 4, 5])
    qtest([7, 5, 4, 6])
    qtest([7, 5, 4, 6, 8])
    qtest([9, 7, 5, 4, 6, 8])

    print("结束")

