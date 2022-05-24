# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def helper(root, p, parent):
            if not root:
                return parent
            
            if (root.val < p.val):
                return helper(root.right, p, parent)
            elif (root.val > p.val):
                return helper(root.left, p, root)
            elif root.val == p.val:
                return helper(root.right, p, parent)
                
        return helper(root, p, None)