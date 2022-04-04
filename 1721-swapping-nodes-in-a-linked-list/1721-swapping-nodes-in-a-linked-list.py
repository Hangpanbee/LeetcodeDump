# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first_node = head
        second_node = head
        dummy = head
        for i in range(1, k):
            first_node = first_node.next
            head = head.next
         
        
        #print(first_node.val)
        while second_node and head.next:
            
            second_node = second_node.next
            head = head.next
  
        #print(second_node.val)
        first_node.val, second_node.val = second_node.val, first_node.val

        
        return dummy
            
        
        