"""
1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creates a dictionary that maps each value to the index of that value.
        # Need dictionary since each entry holes index and distance from target.
        map = {}

        # Iterates through the array checking each number for their matches
        for i, n in enumerate(nums):
            # Calculates what the other number should be to add up to the target
            diff = target - n
            # If match found in dictionary, return the index of that value and the index of the current value.
            if diff in map:
                return [map[diff], i]
            # No match found, add current value and index to dictionary.
            map[n] = i
