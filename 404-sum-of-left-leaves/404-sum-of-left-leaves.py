# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def helper(root, sumLeft, isLeft):
            if not root and isLeft:
                return sumLeft
            elif not root and not isLeft:
                return 0
            
            if isLeft and not root.left and not root.right:
                sumLeft += root.val
                
                
            return helper(root.left, sumLeft, True) + helper(root.right, sumLeft, False)
        
        return helper(root, 0, False)