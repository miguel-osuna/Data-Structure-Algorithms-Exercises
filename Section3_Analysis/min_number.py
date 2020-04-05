""" Write two Python functions to find the minimum number in a list. 
    The first function should compare each number to every other number on the list.
    O(n2). The second function should be linear O(n)."""

import time


def find_min0(num_list):
    start = time.time()
    minimum = min(num_list)
    end = time.time()
    return minimum, end - start


def find_min(num_list):
    """ O(n) time complexity function """
    start = time.time()
    min_num = num_list[0]
    for num in num_list:
        if num < min_num:
            min_num = num

    end = time.time()
    return min_num, end - start


def find_min2(num_list):
    """ O(n^2) time complexity function """
    start = time.time()
    min_num = num_list[0]

    for i in num_list:
        is_smallest = True
        for j in num_list:
            if i > j:
                is_smallest = False
        if is_smallest:
            min_num = i

    end = time.time()
    return min_num, end - start


list_test = [3, -5, -6, 3, 45, -49]
print(find_min0(list_test))
print(find_min(list_test))
print(find_min2(list_test))
