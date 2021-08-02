# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow, fast = head, head.next
        
        # What is the difference between is and ==?
        # is point to an object
        # == compares value
        while slow != fast:
            if fast == None or fast.next == None: return False
            slow = slow.next
            fast = fast.next.next
        
        return True
        