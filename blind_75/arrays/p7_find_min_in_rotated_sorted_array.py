from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid             
        return nums[left]           
    
s = Solution()
nums = [3, 4, 5, 1, 2]
nums = [4, 5, 6, 7, 1, 2, 3]
print(s.findMin(nums))