"""
Topic: 选择排序
Desc : 算法步骤：
            1. 首先在末排序序列中找到最小(大)元素，存放到排序序列的起始位置
            2. 再从剩余末排序元素中继续寻找最小(大)元素，然后存放到已排序序列的末尾
            3. 重复第二步，直到所有元素均排序完毕
"""
import random


def selectSort(list_):
    for i in range(len(list_) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        # i 不是最小数时， 将 i 和最小数进行交换
        if i != min_index:
            list_[i], list_[min_index] = list_[min_index], list_[i]
    return list_


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = selectSort(random_list)
print('选择排序后: ', sort_last)
