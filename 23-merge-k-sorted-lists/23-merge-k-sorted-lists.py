# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return 
        elif len(lists) == 1: return lists[0]

        sorted_ll = self.merge_2_sorted_ll(lists[0], lists[1])
        for i in range(2, len(lists)):
            
            sorted_ll = self.merge_2_sorted_ll(sorted_ll, lists[i])  
        return sorted_ll
        
    def merge_2_sorted_ll(self, l1, l2):
        if not l1: return l2
        elif not l2: return l1
        
        prehead = ListNode(-99999999999)
        curr = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 is not None else l2

        return prehead.next
            
        