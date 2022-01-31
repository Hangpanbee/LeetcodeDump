# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = last = head
        for i in range(n):
            if first: first = first.next
        
        if not first: 
            head = head.next
            return head
        
   
        while first and first.next:
            first = first.next
            last = last.next
        
        
        
       
        last.next = last.next.next
        return head
        
        