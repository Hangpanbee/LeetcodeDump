# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
       
        def dfs(root, index):
            if not root:
                return False
            if index >= len(arr) or root.val != arr[index]:
                return False
            
            if not root.left and not root.right:
                return root.val == arr[index] and index == (len(arr) - 1)

            
            
            return dfs(root.left, index+1) or dfs(root.right, index+1)
        
        
        return dfs(root, 0)