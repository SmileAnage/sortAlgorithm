"""
Topic: 快速排序
Desc : 算法步骤:
            1. 从数列中挑出一个元素，称为'基准'(pivot)
            2. 重新排序数列，所有元素比基准值小的拜访在基准前面，所有元素比准值大的摆在基准的后面(相同的数可以到任一边).
                在这个分区退出之后，该基准就处于数列的中间位置，这个称为分区(partition)操作
            3. 递归地(recursive)把小于基准值元素的子数列和大于基准值元素的子数列排序
"""
import random


def quickSort(list_, left_=None, right_=None):
    left_ = 0 if not isinstance(left_, (int, float)) else left_
    right_ = len(list_) - 1 if not isinstance(right_, (int, float)) else right_
    if left_ < right_:
        partition_index = partition(list_, left_, right_)
        quickSort(list_, left_, partition_index - 1)
        quickSort(list_, partition_index + 1, right_)
    return list_


def partition(list_, left_, right_):
    pivot = left_
    index = pivot + 1
    i = index
    while i <= right_:
        if list_[i] < list_[pivot]:
            swap(list_, i, index)
            index += 1
        i += 1
    swap(list_, pivot, index - 1)
    return index - 1


def swap(list_, i, j):
    list_[i], list_[j] = list_[j], list_[i]


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = quickSort(random_list)
print('快速排序后: ', sort_last)
