# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow = fast = prev = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            

        if slow == head:
            head = None
        elif prev and slow:
            prev.next = slow.next
        
        return head