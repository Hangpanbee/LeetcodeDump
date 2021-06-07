# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
        
            
    def helper(self, root, p, q):
        if root:
            if root == p or root == q:
                return root
            left = self.helper(root.left, p, q)
            right = self.helper(root.right, p, q)
            ## This always hit the leaf node!!
            ## only come here when there nodes left to traverse
            if left and right:
                return root
            if not right:
                return left
            if not left:
                return right

            #have to recurse again
        else: return 
        