# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        seenRight = {}
        ans = []
        def dfs(root, level):
            if not root:
                return
            
            if level not in seenRight:
                ans.append(root.val)
            seenRight[level] = True
            
            right = dfs(root.right, level+1)
            left = dfs(root.left, level+1)
        

        dfs(root, 1)
        return ans