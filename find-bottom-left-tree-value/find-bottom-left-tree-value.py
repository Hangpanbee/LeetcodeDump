# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.helper(root, 0)
        return self.ans[-1]
        
    def helper(self, root, level):
        if root:
            if len(self.ans) == level:
                self.ans.append(root.val)
            self.helper(root.left, level+1)
            self.helper(root.right, level+1)