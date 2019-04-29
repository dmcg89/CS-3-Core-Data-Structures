#!python

from hashtable import HashTable


class Set(object):

    def __init__(self, items = None):
        """Initialize this hash table with the given initial size."""
        self.ht = HashTable()

        if items is not None:
            for item in items:
                self.add(item)
    
    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.ht.keys())
    
    def __iter__(self):
        for item in self.ht.keys():
            yield item 
    
    def contains(self, item):
        return self.ht.contains(item)

    def size(self):
        return self.ht.size

    def add(self, item):
        return self.ht.set(item)
    
    def remove(self, item):
        return self.ht.delete(item)

    def union(self, set2):
        union_set = Set(set2.ht.keys()) # Initialize union set to have contain set 2
        for item in self:
            union_set.add(item)     # add item to set
        return union_set
    
    def intersect(self, set2):
        intersect_set = Set()           # Initialize an empty set
        for item in self:               # Iterate through items in self
            if set2.contains(item):     # Check if item is contained in set 2
                intersect_set.add(item) # Add item to intersect set
        return intersect_set

    def difference(self, set2):
        diff_set = Set()
        for item in self:
            if not set2.contains(item):
                diff_set.add(item)
        return diff_set

    def subset(self, set2):
        if set2.size() > self.size():
            return False
        for item in set2:
            if not self.contains(item):
                return False
        return True