from typing import List
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I aspire for this solution to be second-nature to me one day: 
        # return [ reduce(lambda x,y:x*y,nums[:i]+nums[i+1:]) for i in range(len(nums))]
        # In the meantime...

        array_length = len(nums)
        answer = [1] * array_length

        for i in range (1, array_length):
            answer[i] = answer[i-1] * nums[i-1]
        
        rightProduct = 1
        for i in range(array_length - 1, -1, -1):
            answer[i] *= rightProduct
            rightProduct = rightProduct * nums[i]
        
        return answer

s = Solution()
nums = [1,2,3,4]

print (s.productExceptSelf(nums))