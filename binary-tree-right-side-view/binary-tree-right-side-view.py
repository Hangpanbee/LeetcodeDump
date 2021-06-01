# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def rightSideView(self, root: TreeNode) -> List[int]:
 
        self.helper(root, 0)
        return self.ans
        
    def helper(self, root, level):
        if root:
            print(root.val, level)
            if len(self.ans) == level: self.ans.append(root.val)
            self.helper(root.right, level+1)
            self.helper(root.left, level+1)
  
            return root.val
        