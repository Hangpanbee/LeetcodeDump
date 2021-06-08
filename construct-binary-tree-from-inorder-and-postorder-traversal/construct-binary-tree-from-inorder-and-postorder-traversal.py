# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        return self.helper(inorder, postorder)
        
    def helper(self, inorder, postorder):
        
        # inorder: left side of each root node represent the left tree. Same w right
        # preorder: last value is the root node
        if len(inorder) == 0: return None
        a = TreeNode(postorder.pop())
        a.right = self.helper(inorder[inorder.index(a.val)+1::], postorder)
        a.left = self.helper(inorder[:inorder.index(a.val)], postorder)
        return a
        
        