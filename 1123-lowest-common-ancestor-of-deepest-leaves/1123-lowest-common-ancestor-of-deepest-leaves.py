# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def helper(root, level):
            if not root: return (None, 0)
            
            if not root.left and not root.right: 
                return (root, level)
            
            left = helper(root.left, level+1)
            right = helper(root.right, level+1)
            #print(left, right)
            if left[1] == right[1]:
                return (root, left[1])
            elif left[1] > right[1]:
                return left
            elif right[1] > left[1]:
                return right
            elif left or right:
                return left or right
        
        return helper(root, 0)[0]    
        
        