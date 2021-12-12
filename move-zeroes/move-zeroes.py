class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        tracker = 0
        
        if 0 in nums and len(nums) > 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[tracker], nums[i] = nums[i], nums[tracker]
                    tracker += 1