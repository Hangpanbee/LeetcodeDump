# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool: 
     
        def helper(root, low, high):
            if not root: return True
            
            return low < root.val < high and helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        
        return helper(root, float(-inf), float(inf))
