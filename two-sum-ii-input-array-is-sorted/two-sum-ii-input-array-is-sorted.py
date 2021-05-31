class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] + nums[r] == target: return [l+1, r+1]
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
                
'''
The array is sorted in increasing order.
So, incresing left index gives bigger number and decresing right index gives smaller number.
We start with left index as the 1st index and right index as the last index of the array.
Calculate the sum of the two elements at the two indices.
If it is greater than the target, that means we have to decrese the sum. So, we decrement the right index.
If it is lesser than the target, that means we have to increse the sum. So, we inrement the left index.
Continue this process untill the sum is equal to the target.
'''