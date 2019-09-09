"""
Topic: 冒泡排序
Desc : 算法步骤：
            1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个
            2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数
            3. 针对所有的元素重复以上的步骤，除了最后一个
            4. 持续每次对越来越少的元素重复上面的步骤，知道没有任何一对数字需要比较
"""
import random


def bubbleSort(list_):
    for i in range(len(list_) - 1):
        for j in range(i + 1, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    return list_


random_list = random.sample(range(0, 100), 10)
print('随机列表为: ', random_list)

sort_last = bubbleSort(random_list)
print('冒泡排序后：', sort_last)
