# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinelNode = ListNode(None)
        sentinelNode.next = head
        slow, fast = sentinelNode, head
        while fast:
            if fast and fast.next and fast.val == fast.next.val:
                sillyNode = ListNode(-101)
                while fast and fast.next and fast.val == fast.next.val:
                    fast = fast.next
                sillyNode.next = fast.next

                slow.next = sillyNode
            slow = slow.next
            if fast: fast = fast.next
        
        slow, fast = sentinelNode, sentinelNode.next
        while fast:
            while fast and fast.val == -101:
                fast = fast.next
            slow.next = fast
            slow = slow.next
            if fast: fast = fast.next
        
            
        return sentinelNode.next
            