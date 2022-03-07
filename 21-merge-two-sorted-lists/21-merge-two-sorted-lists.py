# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake_beg = ListNode(-101, None)
        head1 = None
        if l1 and l2:
            if l1.val >= l2.val:
                fake_beg.next = l1
                head1 = l2
            else:
                fake_beg.next = l2
                head1 = l1
        else:
            return l1 if l1 else l2
        
        dummy = fake_beg

        while fake_beg and head1:
            while fake_beg.next and fake_beg.next.val <= head1.val:
                fake_beg = fake_beg.next

            temp = fake_beg.next
            fake_beg.next = head1
            if not temp:
                fake_beg.next = head1
                break
            else:
                fake_beg = temp

            while head1.next and fake_beg and head1.next.val <= fake_beg.val:
                head1 = head1.next
            temp2 = head1.next
            head1.next = temp
            head1 = temp2

            
        return dummy.next
 
        

                
                
        