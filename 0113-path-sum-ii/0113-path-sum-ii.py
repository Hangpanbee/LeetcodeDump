# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths_sum = []
        def traverse(root, remaining, curr):
            if not root: return 
            
            if not root.left and not root.right:
                if remaining-root.val == 0: 
                    curr.append(root.val)
                    paths_sum.append(curr)
                return
            
            currRemaining = remaining - root.val
            traverse(root.left, currRemaining, curr + [root.val])
            traverse(root.right, currRemaining, curr + [root.val])
            return
        
        
        traverse(root, targetSum, [])
        return paths_sum