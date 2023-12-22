class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        # Two words must be the same length to be an anagram.
        if len(s) != len(t):
            return False

        # Initializes an empty dictionary for both words.
        countS = {}
        countT = {}

        # Iterates through the two words, adding each unique letter to dictionary or updating occurrences.
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countT.get(t[i], 0)
        # Iterates through dictionaries and checks if both have the same count for each letter.
        for c in countS:
            if countS[c] != countT.get(c, 0):
                # False returned if difference found in dictionaries.
                return False
        # Both dictionaries iterated through, return True if end reached.
        return True