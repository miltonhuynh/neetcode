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