"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        self.head = Node(10001)
        
        def dfs(root):
            if not root: return (None, None)
            if root.val <= self.head.val:
                self.head = root
            if not root.left and not root.right:
                return (root, root)

            
            l, r = root, root
            left = dfs(root.left)
            if left[1]: 
                left[1].right = root
            if left[0]:
                l = left[0]
            right = dfs(root.right)
            if right[0]: 
                root.right = right[0]
            if right[1]:
                r = right[1]
            return (l, r)
        
        dfs(root)
    
        reverse = self.head
        while reverse.right:
            reverse.right.left = reverse
            reverse = reverse.right
        reverse.right = self.head
        self.head.left = reverse
        
        return self.head