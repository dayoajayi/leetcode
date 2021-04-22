from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return

        q = deque()
        node = head
        # skip the first node and add the rest of the list to a queue
        while node:
            node = node.next
            if not node:
                break
            q.append(node)

        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next
                
            if head and q:
                temp = q.popleft()
                head.next = temp
                head = head.next
        head.next = None

        
'''
https://www.youtube.com/watch?v=To_uAJRu8NQ
'''