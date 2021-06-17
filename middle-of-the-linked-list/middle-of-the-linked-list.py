# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''


fast:                                   v
slow:                  v
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

'''


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        