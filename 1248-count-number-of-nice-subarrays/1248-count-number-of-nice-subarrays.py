class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            countOdds, l, r, res = 0,0,0,0
            
            while r < len(nums):
                countOdds += nums[r] % 2
                while countOdds > k:
                    countOdds -= nums[l] % 2 #shrink window
                    l += 1
                res += r - l + 1
                r += 1
            return res
                        
        return atMost(k) - atMost(k-1)
    
    
'''
T: O(N)
S: O(1)
'''