from typing import List
'''
LC 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
        Because nums[0] + nums[1] == 9, we return [0, 1]

PATTERN: Recognize the inverse operation - we know the target and the store the difference in lookup dictionary. 
         Leverage the concept of 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx, num in enumerate(nums):
            difference = target - num 
            if difference in lookup:
                return [lookup[difference], idx]
            else:
                lookup[num] = idx

nums = [3,2,4]
target = 6
s = Solution()

print(s.twoSum(nums, target))