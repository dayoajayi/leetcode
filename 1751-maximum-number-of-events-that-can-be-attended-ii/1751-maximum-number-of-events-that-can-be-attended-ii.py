class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        
        @lru_cache(None)
        def dp(i, k):
            if i == n:
                return 0
            if k == 0:
                return 0
            
            # option 1: NOT attend event i
            ans = dp(i+1, k)
            
            # option 2: attend event i
            next_i = bisect_left(events, [events[i][1] + 1])
            
            ans = max(ans, events[i][2] + dp(next_i, k-1))
            
            return ans
        
        return dp(0, k)
            
            
'''
T: O(N * K * LogN)

reference: https://youtu.be/QB0thVxL8ZI
'''        
