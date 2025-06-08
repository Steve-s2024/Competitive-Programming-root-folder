# kinda boring, but hey, I did learn some new stuff -> Iterator:
# 31
# ms
# Beats
# 93.78%

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    iterator = None
    record = None
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.record = [self.iterator.next()]

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.record[-1]

    def next(self):
        """
        :rtype: int
        """
        tmp = self.record[-1]
        self.record.append(self.iterator.next())
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        # return self.hasNext
        return self.record[-1] != -100000

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].