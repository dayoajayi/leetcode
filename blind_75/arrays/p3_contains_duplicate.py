class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False

s = Solution()
#nums = [1,2,3,1]
nums = [22,14,18,2,22]

print(s.containsDuplicate(nums))

