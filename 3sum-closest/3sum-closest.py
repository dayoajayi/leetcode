class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        running_best_sum = 1000000 #float('inf')
        
                
        for i in range(0, len(nums) - 2):
        
            if nums[i] == nums[i -1] and i > 0:               #optimization
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:

                s = nums[i] + nums[l] + nums[r]

                if s == target:
                    return s

                if abs(target - s) < abs(target - running_best_sum):
                    running_best_sum = s
                    
                if s <= target:
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1

                else: 
                    r -= 1
                
        return running_best_sum