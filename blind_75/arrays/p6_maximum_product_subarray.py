from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1: return 0
        dp_max = [0]*N
        dp_min = [0]*N

        dp_max[0] = dp_min[0] = nums[0]
        
        for i in range(1,N):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])
            else:
                dp_max[i] = max(dp_min[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_max[i-1]*nums[i], nums[i])
        
        return max(dp_max)

s = Solution()
nums = [2, 3, -2, 4]
nums = [-2, 0, -1]

print(s.maxProduct(nums))