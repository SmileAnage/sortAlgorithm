"""
Topic: 堆排序
Desc : 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
       堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。
算法步骤：
        1. 创建一个堆H[0...n-1]
        2. 把推首(最大值)和堆尾交换
        3. 把堆的尺寸缩小1， 并调用shift_down(0), 目的是把新的数组顶端数据调整到相对于的位置
        4. 重复步骤2， 直到堆的尺寸为1
"""
import random
import math


def buildMaxHeap(list_):
    for i in range(math.floor(len(list_) / 2), -1, -1):
        heapify(list_, i)


def heapify(list_, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < list_len and list_[left] > list_[largest]:
        largest = left
    if right < list_len and list_[right] > list_[largest]:
        largest = right
    if largest != i:
        swap(list_, i, largest)
        heapify(list_, largest)


def swap(list_, i, j):
    list_[i], list_[j] = list_[j], list_[i]


def heapSort(list_):
    global list_len
    list_len = len(list_)
    buildMaxHeap(list_)
    for i in range(len(list_) - 1, 0, -1):
        swap(list_, 0, i)
        list_len -= 1
        heapify(list_, 0)
    return list_


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = heapSort(random_list)
print(' 堆排序后: ', sort_last)
