"""
Topic: 插入排序
Desc : 算法步骤:
            1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是末排序序列
            2. 从头到尾依次扫描末排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
import random


def insertSort(list_):
    for i in range(list_):
        pre_index = i - 1
        current = list_[i]
        while pre_index >= 0 and list_[pre_index] > current:
            list_[pre_index + 1] = list_[pre_index]
            pre_index -= 1
        list_[pre_index + 1] = current
    return list_


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = insertSort(random_list)
print('选择排序后: ', sort_last)
