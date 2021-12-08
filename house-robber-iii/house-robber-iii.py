# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return [0, 0]
            
            left_val = dfs(root.left)
            right_val = dfs(root.right)
            neighbor_max_val = left_val[1] + right_val[1]
            curr_max_value = max(left_val[0] + right_val[0] + root.val, neighbor_max_val)
            
            #[max_val_of_2_houses_down, max_val_of_neighbor]
            return [neighbor_max_val, curr_max_value]
        
        return max(dfs(root))
            
            
        