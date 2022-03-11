# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k == 0: return head
        ans = head2 = head3 = head
        size = 1
        while head.next:
            size += 1
            head = head.next
        
        move_to_the_right_size =  k % size
        if move_to_the_right_size == 0: return ans
        for i in range(size - move_to_the_right_size - 1):
            ans = ans.next
        #print(ans)
        tmp = ans.next
        ans.next = None
        head.next = head2
        return tmp
        