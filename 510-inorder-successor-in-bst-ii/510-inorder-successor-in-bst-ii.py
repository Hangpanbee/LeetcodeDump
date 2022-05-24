"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        
        def dfs(root, p, parent):
            if not root: return parent
            if root.val <= p.val:
                return dfs(root.right, p, parent)
            elif root.val > p.val:
                return dfs(root.left, p, root)

        if node.right: 
            
            return dfs(node.right, node, None)   
        else:
            curr = node.parent
            while curr:
                if node.val < curr.val: 
                    return curr
                else:
                    curr = curr.parent
            return None