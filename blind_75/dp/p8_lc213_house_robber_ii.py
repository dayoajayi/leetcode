from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        
        dp1, dp2 = 0,0
        for n in nums[:-1]:
            tmp = dp1
            dp1 = max(dp2+n, dp1)
            dp2 = tmp

        dpp1, dpp2 = 0,0
        for n in nums[1:]:
            tmp = dpp1
            dpp1 = max(dpp2+n, dpp1)
            dpp2 = tmp

        return max(dp1, dpp1)

nums = [2,3,2]
s = Solution()

print(s.rob(nums))


# T: O(N)
# S: O(1)