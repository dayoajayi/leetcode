class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False

s = Solution()
#nums = [1,2,3,1]
nums = [22,14,18,2,22]

print(s.containsDuplicate(nums))

'''
Since a set only store unique objects, I store the input in a set and compare the length to 
that of the original array

T: O(1)
S: O(1)