class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        
        if len(nums) < 3:
            return []
        
                
        for i in range(len(nums) - 2):
        
            if nums[i] > 0: 
                break
                
            if nums[i] > 0 and nums[i] == nums[i -1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:

                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    triplets.append((nums[i], nums[l], nums[r]))
                    l += 1

                elif s < 0:
                    l += 1

                else: 
                    r -= 1
                
        return list(set(triplets))