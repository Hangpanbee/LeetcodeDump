# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        slow = fast = connect = headA 
        while connect.next:
            connect = connect.next
        connect.next = headB
        
        
        ans = None
        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
 
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow = slow.next
                    if not fast.next:
                        fast = headB
                    else: fast = fast.next
                ans = slow
                break
        connect.next = None
                
        return ans
                