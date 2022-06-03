# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete = {node: True for node in to_delete}
        ans = []
        if root.val not in toDelete: ans.append(root)
        def traverse(root):
            if not root: return
            
            left = root.left
            right = root.right
            if root.left and root.left.val in toDelete:
                root.left = None
            if root.right and root.right.val in toDelete:
                root.right = None
            
            if root.val in toDelete:
                if root.left and root.left.val not in toDelete: ans.append(left)
                if root.right and root.right.val not in toDelete: ans.append(right)
                root.left, root.right = None, None
            
            traverse(left)
            traverse(right)
            
        traverse(root)
        
        return ans
            