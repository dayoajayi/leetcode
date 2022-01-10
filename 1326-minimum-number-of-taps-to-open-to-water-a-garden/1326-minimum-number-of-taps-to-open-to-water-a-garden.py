class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jumps = [0] * (n + 1)
        for x, r in enumerate(ranges):
            l = max(0, x-r)
            jumps[l] = max(jumps[l], x+r)
            
        step, start, end = 0, 0, 0
        while end < n:
            start, end = end + 1, max(jumps[start:end+1])
            if start > end:
                return -1
            step += 1
        return step          
        
        
'''
T: O(N)
S: O(N)

Ref: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484299/Python-%3A-O(N)
'''