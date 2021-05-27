class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        curr = 0
        r = len(nums) - 1
        
        while curr <= r:
            if nums[curr] == 2:
                self.swap(nums,curr, r)
                r -= 1
            elif nums[curr] == 0:
                self.swap(nums, curr, l)
                curr += 1
                l += 1
            else:
                curr += 1
                
        
    def swap(self, nums, i, j):
        hold = nums[i]
        nums[i] = nums[j]
        nums[j] = hold