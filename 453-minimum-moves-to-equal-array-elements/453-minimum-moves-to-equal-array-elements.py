class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            
            moves += nums[i] - nums[0]

        return moves
    
'''
T: O(nlogn)
S: O(1)

https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93905/Four-Python-solutions-with-detailed-explanation
'''