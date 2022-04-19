# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.problem1, self.problem2, self.problem3 = None, None, None
        self.tip = None
        ans = []
        def dfs2(root):
            if not root: return
            
            dfs2(root.left)
            if self.tip and root.val < self.tip.val:
                if not self.problem1: self.problem1 = self.tip
                if not self.problem2: self.problem2 = root
                self.problem3 = root
            self.tip = root
            ans.append(root)
            dfs2(root.right)
            
            
        dfs2(root)
        
        ans = [self.problem1, self.problem2, self.problem3]
        
        newAns = [self.problem1.val, self.problem2.val, self.problem3.val]
        newAns.sort()
   
        
        
        for i in range(len(ans)):
            ans[i].val = newAns[i]
        
    