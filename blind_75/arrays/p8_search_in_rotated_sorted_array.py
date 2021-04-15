from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N - 1

        # first determine the pivot point in the ROTATED array
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        
        # then do a regular binary search
        left, right = 0, N-1
        while (left <= right):
            mid = (left + right) // 2
            mid2 = (mid+pivot) % N  # mid2 is the "real" midpoint from the unrotated array
            if nums[mid2] == target:
                return mid2
            elif nums[mid2] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


        

s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0

print(s.search(nums, target))