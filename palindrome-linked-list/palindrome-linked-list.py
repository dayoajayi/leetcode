# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        
        # store the linked list in an array
        while head:
            nums.append(head.val)
            head = head.next
            
        # initiate left and right pointers to check palindrome
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
            
        return True