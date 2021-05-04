from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        start = maxlen = 0
        lookup = {}
          
        for idx, char in enumerate(s):
            if char in lookup and start <= lookup[char]:
                start = lookup[char]+1
            else:
                maxlen = max(maxlen, idx - start + 1)
            lookup[char] = idx

        return maxlen

sol = Solution()

s = "abcabcbb"  
print(sol.lengthOfLongestSubstring(s))
# answer: 3
