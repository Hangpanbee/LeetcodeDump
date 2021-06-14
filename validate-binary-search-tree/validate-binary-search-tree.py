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
		    if root.left and (low >= root.left.val  or root.left.val >=  high or root.left.val >= root.val): return False
		    if root.right and (low >= root.right.val or root.right.val >= high or root.right.val <= root.val): return False
		    left = helper(root.left, low, root.val)
		    right = helper(root.right, root.val, high)
		    return left and right
	    return helper(root, -float(inf), float(inf))


