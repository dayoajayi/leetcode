from typing import List
'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to 
target. If there is no such subarray, return 0 instead.

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = window_size = l = r = 0
        N = len(nums)

        for num in range(len(nums)):
            # advance the right pointer, 
            # update the running sum 
            # update the window_size (return value) 
            running_sum += nums[num]
            
            while running_sum >= target:
                # shrink the window from the left side
                window_size = min(window_size, num-l+1)
                running_sum -= nums[l]+1
        return window_size
            
                
nums = ["2, 3, 1, 2, 4, 3"]
target = 7
s = Solution()

print(s.minSubArrayLen(nums, target))
you
