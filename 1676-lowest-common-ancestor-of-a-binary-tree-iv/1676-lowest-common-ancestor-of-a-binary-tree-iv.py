# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodesCounter = {}
        for i, v in enumerate(nodes):
            nodesCounter[v.val] = True
        
        def helper(root):
            if not root: return None
            
            if root.val in nodesCounter:
                return root
            
            left = helper(root.left)
            right = helper(root.right)
            #print(left, right, root.val)
            if left and right:
                return root
            elif left or right:
                return left or right
            
        a = helper(root)
        #print(a)
        return a
            
            