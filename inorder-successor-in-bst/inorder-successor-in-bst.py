# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        def helper(root, p, potentSuccessor):
            if not root: return potentSuccessor
            elif root.val > p.val: return helper(root.left, p, root)
            elif root.val <= p.val: return helper(root.right, p, potentSuccessor) 
                
        return helper(root, p, None)
        
        