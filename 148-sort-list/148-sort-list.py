# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return 
        #merge sort of linkedlist
        def getLLlenAndMap(head):
            mapLenToNode = {}
            lenLL = 0
            while head:
                mapLenToNode[lenLL] = head
                head = head.next
                mapLenToNode[lenLL].next = None
                lenLL += 1
            return (lenLL, mapLenToNode)
        
        
        def partition(l, h):
            if h == l:
        
                return mapLenToNode[l]
            paritioned = l + (h-l)//2
            
            firstLL = partition(l, paritioned)
            secndLL = partition(paritioned+1, h)
            return mergeSort(firstLL, secndLL, h-l)
            
            
        def mergeSort(firstLL, scndLL, countRun):
            l, r = 0, 0
            ans = ListNode(0)
            dummy = ans
            #print("IN", firstLL, scndLL, countRun)
            while firstLL and scndLL:
                if firstLL.val >= scndLL.val:
                    ans.next = ans = ListNode(scndLL.val)
        
                    scndLL = scndLL.next
                elif firstLL.val < scndLL.val:
                    ans.next = ans = ListNode(firstLL.val)
                    firstLL = firstLL.next
            #print(firstLL, scndLL)
            if firstLL:
                ans.next = firstLL
            elif scndLL:
                ans.next = scndLL
            #print("OUT", dummy)
            return dummy.next
        
        lenLL, mapLenToNode = getLLlenAndMap(head)
        #print(mapLenToNode)
        a = partition(0, lenLL-1)
        
        #print(a)
        return a
        
            
            