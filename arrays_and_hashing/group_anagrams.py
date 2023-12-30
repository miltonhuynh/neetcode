"""
49. Group Anagrams (Easy)
https://leetcode.com/problems/group-anagrams
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creates a dictionary that maps the character count to list of anagrams.
        answer = {}

        