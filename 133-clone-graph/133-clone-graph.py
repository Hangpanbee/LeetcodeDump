"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        
        nodeCopy = Node(node.val, [])
        graphRep = {node.val: nodeCopy}
        stack = [node]

        
        while stack:
            currNode = stack.pop()
            
            for neighbor in currNode.neighbors:
                if neighbor.val not in graphRep: 
                    graphRep[neighbor.val] = Node(neighbor.val, [])
                    stack.append(neighbor)
                graphRep[currNode.val].neighbors.append(graphRep[neighbor.val])
        

        return nodeCopy
        
        
        