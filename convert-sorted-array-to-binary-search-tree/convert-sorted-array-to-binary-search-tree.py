# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Intuition: since this is a sorted array, I'll need to apply binary search SOMEHOW!!
        
        1. Calculate the midpoint of the array
        2. Use the midpoint as the root of the array
        3. Recursively call a helper method on the left of the tree and right of the tree
            3a. Base case: while tree is not null
            
        '''
        
        
        def bstHelper(l, r):            
            if l > r:
                return None
            
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = bstHelper(l, mid - 1)
            root.right = bstHelper(mid + 1, r)

            return root
        
        return bstHelper(0, len(nums) - 1)