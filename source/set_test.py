#!python

from sets import Set
#
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
# if not hasattr(unittest.TestCase, 'assertCountEqual'):
#     unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):
    def test_init(self):
        set1 = Set()
        assert set1.size() == 0

    def test_contains(self):
        set1 = Set([1, 2, 3])
        assert set1.contains(1) == True
        assert set1.contains(2) == True
        assert set1.contains(3) == True
    
    def test_add_and_contains(self):
        set1 = Set()
        set1.add(1)
        set1.add(2)
        assert set1.contains(1) == True
        assert set1.contains(2) == True
        assert set1.contains(3) == False
    
    def test_delete(self):
        set1 = Set([1, 2, 3])
        set1.remove(1)
        assert set1.size() == 2
        assert set1.contains(1) == False
        set1.remove(2)
        assert set1.size() == 1
        assert set1.contains(2) == False
        set1.remove(3)
        assert set1.contains(3) == False
        assert set1.size() == 0
        
    def test_union(self):
        set1 = Set([1, 2, 3])
        set2 = Set([3, 4, 5])
        union_set = set1.union(set2)
        assert union_set.contains(1)
        assert union_set.contains(2)
        assert union_set.contains(3)
        assert union_set.contains(4)
        assert union_set.contains(5)
        assert union_set.size() == 5

    def test_intersection(self):
        set1 = Set([1, 2, 3])
        set2 = Set([2, 3, 4])
        intersect_set = set1.intersect(set2)
        assert intersect_set.contains(2) == True
        assert intersect_set.contains(3) == True
        assert intersect_set.contains(1) == False
        assert intersect_set.contains(4) == False
        assert intersect_set.size() == 2
    
    def test_difference(self):
        set1 = Set([1, 2, 3])
        set2 = Set([2, 3, 4])
        diff_set = set1.difference(set2)
        assert diff_set.contains(1) == True
        assert diff_set.contains(4) == False
        assert diff_set.contains(2) == False
        assert diff_set.contains(3) == False
        assert diff_set.size() == 1
        diff_set2 = set2.difference(set1)
        assert diff_set2.size() == 1
        assert diff_set2.contains(4) == True
    
    def test_subset(self):
        set1 = Set([1, 2, 3])
        set2 = Set([2, 3, 4])
        set3 = Set([2, 3])
        subset1 = set1.subset(set2)
        subset2 = set1.subset(set3)
        assert subset1 == False
        assert subset2 == True
        subset3 = set3.subset(set1)
        assert subset3 == False

