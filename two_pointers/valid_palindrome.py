"""
125. Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome
"""

"""
Not optimal solution, uses built-in functions and extra memory.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initializes a new empty string to store new string with only alphanumeric characters
        newStr = ""

        # Iterates through input string and adds to new string if character is alphanumeric.
        for i in s:
            if i.isalnum():
                # Ignores cases
                newStr += i.lower()
        # Returns true if new string and its reverse are equivalent
        return newStr == newStr[::-1]


"""
Optimal solution, does not use extra memory.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Converts string to all capital letters to ignore case.
        s = s.upper()
        # Initializes pointers at beginning and end of string.
        left = 0
        right = len(s) - 1
        # Runs until 2 pointers meet in the middle
        while left <= right:
            # If left or right pointer is not alphanumeric, move onto the next
            if s[left].isalnum() == False:
                left += 1
                # Continue prevents comparison from being done.
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            # Compares the next 2 pointers
            left += 1
            right -= 1
        # No mismatch found, returns True.
        return True