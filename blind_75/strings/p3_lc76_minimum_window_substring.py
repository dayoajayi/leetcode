from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter (t)
        max = float('inf')
        output = ''
        S = len(s)
        start, end = 0, 0
        count = len(lookup)

        while end < S:
            # move the end pointer to slide to the right    
            while end < S and count != 0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        count -= 1
                end+=1
            
            # move the start pointer
            while start < end and count == 0:
                if end-start < max:
                    max = end-start
                    output = s[start:end]
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    if lookup[s[start]] > 0:
                        count += 1
                start+=1
        return output

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"

print(sol.minWindow(s,t))



'''
Given two strings s and t, return the minimum window in s which will contain all 
the characters in t. If there is no such window in s that covers all characters in t,
 return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only 
one unique minimum window in s.

https://leetcode.com/problems/minimum-window-substring/
'''