"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        newNode = Node(insertVal, None)
        if not head: 
            newNode.next = newNode
            return newNode
        dummy = head
        while head:
            pivot_start_pt = insertVal < head.next.val < head.val
            end_pivot_pt = head.next.val < head.val < insertVal
            not_a_pivot = head.val <= insertVal <= head.next.val

            if pivot_start_pt or end_pivot_pt or not_a_pivot or head.next == dummy:
                tmp = head.next
                head.next = newNode
                newNode.next = tmp
                break    
            head = head.next


        return dummy