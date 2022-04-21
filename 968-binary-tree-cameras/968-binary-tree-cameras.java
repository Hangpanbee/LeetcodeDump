# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        CAMERA = 1
        MONITORED = 2
        UNMONITORED = 0
        @lru_cache(None)
        def dfs(root, state):
            if not root: 
                return 1 if state == CAMERA else 0
            
        
            withCamera = 1 + dfs(root.left, MONITORED) + dfs(root.right, MONITORED)
            #print(withCamera)
            
            if state == MONITORED:
                withoutCamera = dfs(root.left, UNMONITORED) + dfs(root.right, UNMONITORED)
            elif state == UNMONITORED and (root.left or root.right):
                withoutCamera = min(dfs(root.left, CAMERA) + dfs(root.right, UNMONITORED), dfs(root.left, UNMONITORED) + dfs(root.right, CAMERA))
                
            else:
                withoutCamera = 999999999
          
            return min(withCamera, withoutCamera)
        
        
        return dfs(root, UNMONITORED)