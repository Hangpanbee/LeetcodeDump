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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def dfs(root, targetNode):
            if not root: return False
            if root.val == targetNode.val: return True
            left = dfs(root.left, targetNode)
            right = dfs(root.right, targetNode)
            return left or right
        
        if dfs(p, q):
            return p
        elif dfs(q, p):
            return q
        else:
            seen = {}
            while p:
                seen[p] = True
                p = p.parent
            while q:
                if q in seen: return q
                q = q.parent
        