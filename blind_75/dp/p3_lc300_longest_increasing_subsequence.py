from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        N = len(nums)
        dp = [1] * N
        count = [1] * N

        for i in range (N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1 )                    
        return max(dp)

#nums = [10,9,2,5,3,7,101,18]
#nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
s = Solution()
print(s.lengthOfLIS(nums))