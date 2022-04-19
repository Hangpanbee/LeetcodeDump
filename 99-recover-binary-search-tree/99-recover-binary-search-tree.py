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
        
        self.problem1, self.problem2 = None, None
        ans = []
        def dfs2(root):
            if not root: return
            
            dfs2(root.left)
            ans.append(root)
            dfs2(root.right)
            
            
        dfs2(root)
        newans = sorted(ans, key=lambda x: x.val)
 
        for i in range(len(ans)):
            if ans[i] != newans[i]:
                if not self.problem1: self.problem1 = ans[i]
                self.problem2 = ans[i]
        
        self.problem1.val, self.problem2.val = self.problem2.val, self.problem1.val
        #print(self.problem1, self.problem2)