"""
20. Valid Parenthesis (Easy)
https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Creates a python list to simulate a stack.
        stack = []
        # Creates a map of each opening to its closing.
        # Keys: closing
        # Values: opening
        Map = {")": "(", "]": "[", "}": "{"}
        # Iterate through and check each character in string.
        for char in s:
            # Checks if character is closing, all keys in map are closing parenthesis.
            if char in Map:
                # If stack is not empty and top of stack (closing) matches opening, pop from stack
                if stack and stack[-1] == Map[char]:
                    stack.pop()
                # No corresponding opening to close, return False
                else:
                    return False
            # Character is opening, add to top of stack
            else:
                stack.append(char)
        # Stack must be empty at end to return True.
        return True if not stack else False


