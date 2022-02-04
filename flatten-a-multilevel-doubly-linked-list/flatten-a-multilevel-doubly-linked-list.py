"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        def dfs(head, removed_next):
            if not head: return
            if not head.next and removed_next: 
                head.next = removed_next
                removed_next.prev = head
                removed_next = None

            child = dfs(head.child, removed_next)
            if child: 
                tmp = head.next
                head.next = child
                child.prev = head
                #print("child", head.val, child.val)
                head.child = None
                next_node = dfs(head.next, tmp)
            else:
                head.child = None
                next_node = dfs(head.next, removed_next)
            return head
        
        dfs(head, None)

        return head