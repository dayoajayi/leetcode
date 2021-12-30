class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        nums = [1,7,3,6,5,6]        
        '''        
        pivot = -1
        left = 0
        right = sum(nums)
        
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                pivot = i
                break
            left += nums[i]                 
        return pivot