class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        
        for i in range(len(nums)+1):
            if i not in c:
                return i