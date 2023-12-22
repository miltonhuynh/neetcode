"""
217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/
"""

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initializes a set to store unique numbers, uses a set instead of an array because adding is O(1) instead of O(N).
        nums_set = set()
        # Iterates through input array of numbers.
        for n in nums:
            # Number already found in set, return True.
            if n in nums_set:
                return True
            # Number not in set, add it to the set.
            else:
                nums_set.add(n)
        # Finished iterating through array, duplicate was never found.
        return False

