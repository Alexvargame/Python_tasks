# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.integers = deque()
        self.flatten(nestedList)

    def flatten(self, integers):
        for elem in integers:
            if elem.isIntegers():
                self.integers.append(elem.getInteger())
            else:
                self.flatten(elem.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.integers.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.integers) > 0


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.iter = self.iterate(nestedList, top_level=True)
        self.next_value = next(self.iter)


    def iterate(self, nested_list, top_level=False):
        for nested_elem in nested_list:
            if nested_elem.isIntegers():
                yield nested_elem.getInteger()
            else:
                yield from self.iterate(nested_elem.getList())
        if top_level:
            yield None

    def next(self):
        """
        :rtype: int
        """
        return_value = self.next_value
        self.next_value = next(self.iter)
        return return_value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.a is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


def main():
    pass
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    #print('res', carFleet(10, [6, 8], [3, 2]))



if __name__ == "__main__":
    main()
