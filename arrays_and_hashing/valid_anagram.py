class Solution(object):
    def isAnagram(self, s, t):
        s_set = set()
        t_set = set()

        for i in s:
            s_set.add(i)
        for i in t:
            t_set.add(i)

        print(s_set)
        print(t_set)

        if s_set == t_set:
            return True

        else:
            return False


test = Solution()
s = ["cat"]
t = ["tac"]
print(test.isAnagram(s,t))

