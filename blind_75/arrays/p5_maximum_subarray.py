from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum, current_sum = float('-inf'), 0

        for num in nums:
            current_sum = max(current_sum+num, num)
            global_sum = max(global_sum,current_sum)

        return global_sum

s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [5, 4, -1, 7, 8]

print(s.maxSubArray(nums))