class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for i in range(len(nums)):
            if i == nums[i]:
                i += 1
            else:
                return i       
        return i
        
        
        
        '''
        c = collections.Counter(nums)
        
        for i in range(len(nums)+1):
            if i not in c:
                return i
        '''