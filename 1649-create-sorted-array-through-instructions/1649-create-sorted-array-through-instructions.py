from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
            [ 1, 5, 6, 2]
            [1]
            [1,5]
            [1,5,6]
            [1,2,5,6]
            think about duplicate
        """
        arr = SortedList()
        m = 10**9 + 7
        sumCost = 0
        for i, instruction in enumerate(instructions):
            s, l = self.update(arr, instruction)
            sumCost += min(s, l) % m
        
  
        return sumCost % m
        
        
        
    def update(self, arr, target):
        si = arr.bisect_left(target)
        arr.add(target)
        li = len(arr) - arr.bisect_right(target) 
        
        
        return (si, li)