# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.beginning = head
        self.ans = True
        def helper(head):
            if not head: 
                return head
            
            dummy = helper(head.next)
            if dummy:
                self.ans = dummy.val == self.beginning.val and self.ans
                #print(dummy, self.beginning, self.ans)
                self.beginning = self.beginning.next
            return head
        
        helper(head)
        return self.ans
        
        
        