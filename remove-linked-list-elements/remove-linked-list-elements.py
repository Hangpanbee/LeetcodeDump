# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        currHead = removedHead = head
        
        while removedHead and removedHead.next:
            if removedHead.next.val != val:
                #print(currHead.val, removedHead.next.val )
                currHead.next = removedHead.next
                #print(head)
                currHead = removedHead.next
            removedHead = removedHead.next
        currHead.next = removedHead.next
        #print(currHead)
        if head.val == val:
            head = head.next
        return head
                
        