# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        return self.helper(p,q)
    
    def helper(self, p, q):
        if not p and q: 
            return False
        if not q and p: 
            return False
        if not q and not p: return True
        if p.val != q.val: return False
        return p.val == q.val and self.helper(p.left, q.left) and self.helper(p.right, q.right)
        
    