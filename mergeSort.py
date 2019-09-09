"""
Topic: 归并算法
Desc : 算法步骤：
            1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
            2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
            3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
            4. 重复步骤3，直到某一指针达到序列尾
            5. 将另一序列剩下的所有元素直接复制到合并序列尾
"""
import random
import math


def mergeSort(list_):
    if len(list_) < 2:
        return list_
    middle = math.floor(len(list_) / 2)
    left, right = list_[0:middle], list_[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left_, right_):
    result = []
    while left_ and right_:
        if left_[0] <= right_[0]:
            result.append(left_.pop(0))
        else:
            result.append(right_.pop(0))
    while left_:
        result.append(left_.pop(0))
    while right_:
        result.append(right_.pop(0))
    return result


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = mergeSort(random_list)
print('归并排序后: ', sort_last)