# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val > q.val:
            p, q = q, p
        # so that p < q
        def helper(root, p1, q1):
            left, right = None, None
            if not root: return root
            if (root.val < p.val):
                right = helper(root.right, p1, q1)
            elif (root.val == p.val or root.val == q.val):
                return root
            elif (root.val > q.val):
                left = helper(root.left, p1, q1)
            else: return root
            
            if left or right:
                return left or right
            
        a = helper(root, p, q)
        
        return a if a != p and a!=p else p or q