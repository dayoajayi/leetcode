class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for element in nums:
            for i in range(len(result)):
                result.append(result[i] + [element])
                
        return result
    
    
'''
Time: O(n*2^n)
Space: O(n*2^n)
'''