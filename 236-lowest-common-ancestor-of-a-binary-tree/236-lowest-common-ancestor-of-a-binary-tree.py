# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
        
            
    def helper(self, root, p, q):
        ## return False early will save a lot of time in term of runtime
        if not root or root == p or root == q :
            return root
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        ## only get to this part if it is at the leaf node
        if left and right:
            return root
        if not right:
            return left
        if not left:
            return right

        