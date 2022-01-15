class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallestPositive = 1
        for num in nums:
            if num == smallestPositive:
                smallestPositive += 1
        return smallestPositive
    
'''
T: O(NLogN)
'''