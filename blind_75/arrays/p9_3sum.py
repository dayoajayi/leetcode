from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, result = len(nums), []
       
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            start, end = i+1, N-1
            while start < end:
                if nums[start] + nums[end] == target:
                    result.append([nums[i], nums[start], nums[end]])
                    start = start + 1
                    while start < end and nums[start] == nums[start-1]:
                        start = start + 1
                elif nums[start] + nums[end] < target:
                    start = start + 1
                else:
                    end = end - 1
        return result

            
s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))