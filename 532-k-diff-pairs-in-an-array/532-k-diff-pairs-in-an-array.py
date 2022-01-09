class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        numPairs = 0
        
        if k == 0:
            for key, val in count.items():
                if val > 1:
                    numPairs += 1
        else:        
            for key, val in count.items():
                if key + k in count:
                    numPairs += 1
        return numPairs
                                   
                    
                
        
'''
T: O(N^2)
S: O(N)
'''