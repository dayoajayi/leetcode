# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True # we have a cycle
            else:
                seen.add(curr)
                curr = curr.next
        return False