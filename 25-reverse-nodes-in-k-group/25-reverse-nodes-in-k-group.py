# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        ans = None
        slow = ListNode(val=0, next=head)
        fast = head
        curr_sub_len = 1
        while fast:
            
            if curr_sub_len%k == 0:
                temp = fast.next
                fast.next = None
                head_of_group = slow.next
                slow.next = None
                new_head = self.reverseGroup(head_of_group)
                if head_of_group == head:
                    ans = new_head
                slow.next = new_head
                head_of_group.next = temp
                fast = slow = head_of_group
                
            curr_sub_len += 1
            fast = fast.next
 
        return ans
        
        
    
    def reverseGroup(self, curr):
        prev = None
        while curr:
            currNext_temp = curr.next
            curr.next = prev
            prev = curr
            curr = currNext_temp
  
        return prev