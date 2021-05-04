from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        
        for t in range (1, target+1):
            for n in nums:
                if n < t:
                    dp[t] += dp[t-n]
                    
        return dp[target]

nums = [1,2,3]
target = 4

s = Solution()

print(s.combinationSum4(nums,target))