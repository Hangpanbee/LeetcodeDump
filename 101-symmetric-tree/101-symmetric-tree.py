# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 and root2:
                return False
            elif root1 and not root2:
                return False
            
            
            return root1.val == root2.val and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        
        return dfs(root.left, root.right)