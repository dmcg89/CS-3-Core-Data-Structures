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
        linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively
    if len(array) == 0: # if array is empty return none
        return None
    middle_index =  len(array) // 2     # Use floor division to return integer
    chances = len(array) - 1
    while chances > 0:
        if item == array[middle_index]: # item is at middle index
            return middle_index
        if item < array[middle_index]:
            middle_index = middle_index // 2
            chances -= 1
        elif item > array[middle_index]:
            # middle_index += middle_index // 2
            middle_index = middle_index + (len(array) - middle_index) // 2
            chances -= 1
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # implement binary search recursively here
    if len(array) == 0:
        return None
    middle_index = len(array) // 2      # Use floor division to return integer
    if item == array(middle_index):
        return middle_index
    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

# names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
# linear_search_recursive(names, 'Kojin', index=0)
