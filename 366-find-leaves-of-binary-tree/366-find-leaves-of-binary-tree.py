# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        def dfs(root):
            if not root: return -1
            
            
            left = dfs(root.left)
            right = dfs(root.right)
            currLevel = 1 + max(left, right)
            if len(ans) <= currLevel:
                ans.append([])
                ans[currLevel] = [root.val]
            else:
                ans[currLevel].append(root.val)
                
            return currLevel
        
        dfs(root)
        return ans