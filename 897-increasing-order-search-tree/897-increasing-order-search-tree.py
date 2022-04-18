# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = None
        def dfs(root, parent):
            if not root: return parent
            
            left = dfs(root.left, root)
            if not self.ans: self.ans = root
            root.left = None
           
            root.right = dfs(root.right, parent)
           
            return left
        
        a = dfs(root, None)
        return a