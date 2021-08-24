# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
                
        def checkBST(root, l, r):
            if root: 
                if l < root.val and r > root.val:
                    if checkBST(root.left, l, root.val) and checkBST(root.right, root.val, r):
                        return True
                return False
            return True            
    
        return checkBST(root, float("-inf"), float("inf"))