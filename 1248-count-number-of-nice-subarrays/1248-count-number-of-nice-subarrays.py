class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            l,r, countOdds, result = 0, 0, 0, 0
            while r < len(nums):
                countOdds += nums[r] % 2
                while countOdds > k:  #shrink window
                    countOdds -= nums[l] % 2
                    l += 1
                result += r - l + 1
                r += 1
            return result
        
        return atMost(k) - atMost(k-1)
'''
T: O(N)
S: O(1)
'''