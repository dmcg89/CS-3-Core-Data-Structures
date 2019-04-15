#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if index == len(array):   #  reached end of list without finding item  
        return None
    elif item == array[index]:
        return index
    else:                       # if index is still in range, search next item
        return linear_search_recursive(array, item, index + 1 )

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)

def binary_search_iterative(array, item):
    # implement binary search iteratively
    left = 0
    right = len(array) - 1
    while left <= right:
        median_index = (left + right) // 2
        median_value = array[median_index]

        if median_value == item:
            return median_index
        
        if item > median_value:
            left = median_index + 1
        else:
            right = median_index - 1

def binary_search_recursive(array, item, left=0, right=None):
    # implement binary search recursively here

    if right == None:  
        right = len(array) - 1
    elif left > right:
        return None
    median_index = (right + left) // 2
    median_value = array[median_index]
    if median_value == item:
        return median_index
    elif item > median_value:
        left = median_index + 1
    elif item < median_value:
        right = median_index - 1
    
    return binary_search_recursive(array, item, left, right)