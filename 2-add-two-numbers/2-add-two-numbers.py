# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        
        carryOver = 0
        sumL = dummy = ListNode(0)
        
        while l1 or l2 or carryOver:
            currSum = carryOver
            if l1:
                currSum += l1.val
                l1 = l1.next
            if l2:
                currSum += l2.val
                l2 = l2.next
            
            if currSum >= 10:
                carryOver =1
                currSum %= 10
            else:
                carryOver = 0
            sumL.next = sumL = ListNode(currSum)    
        
        
  
        return dummy.next
            