# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return None
            newTree = TreeNode()
            if root1 and root2:
                newTree.val = root1.val+root2.val
                newTree.left = dfs(root1.left, root2.left)
                newTree.right = dfs(root1.right, root2.right)
            elif root1:
                newTree.val = root1.val
                newTree.left = dfs(root1.left, root2)
                newTree.right = dfs(root1.right, root2)
            elif root2:
                newTree.val = root2.val
                newTree.left = dfs(root1, root2.left)
                newTree.right = dfs(root1, root2.right)
                
                
            return newTree
        
        return dfs(root1, root2)