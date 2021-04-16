from collections import Counter
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count

s = 'anagram'
t = 'nagaram'

sol = Solution()
print(sol.isAnagram(s,t))