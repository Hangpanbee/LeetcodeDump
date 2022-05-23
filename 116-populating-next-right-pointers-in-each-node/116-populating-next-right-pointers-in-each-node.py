"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        ## next try: try to solve it using parent node. next pointer! but use recursion
        
        nodeLevelMap = collections.defaultdict(list)
        self.helper(root, nodeLevelMap, 0)
        return root
        
    def helper(self, root, nodeLevelMap, level):
        if not root: return
        nodeLevelMap[level].append(root)
        self.helper(root.left, nodeLevelMap, level+1)
        self.helper(root.right, nodeLevelMap, level+1)
        if len(nodeLevelMap[level]) > 1:    
            nodeLevelMap[level][-2].next = root
        if len(nodeLevelMap[level]) == 2**level: 
            root.next = None
        
        