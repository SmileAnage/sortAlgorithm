"""
Topic: 希尔排序
Desc : 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
算法步骤：
    1. 选择一个增量序列t1, t2, ……, tk, 其中 ti > tj, tk = 1
    2. 按增量序列个数k, 对序列进行k趟排序
    3. 每趟排序，根据对应的增量ti,将待排序序列分割成若干长度为m的子序列，分贝对各子表进行直接插入排序。
        仅增量因为1时，整个序列作为一个表来处理，表长度既为整个序列的长度
"""
import random
import math


def shellSort(list_):
    gap = 1
    while gap < len(list_) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(list_)):
            temp = list_[i]
            j = i - gap
            while j >= 0 and list_[j] > temp:
                list_[j + gap] = list_[j]
                j -= gap
            list_[j + gap] = temp
        gap = math.floor(gap / 3)
    return list_


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = shellSort(random_list)
print('希尔排序后: ', sort_last)
