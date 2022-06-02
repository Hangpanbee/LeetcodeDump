class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        startCounter = collections.Counter(start)
        endCounter = collections.Counter(end)
        sameCount = endCounter - startCounter
        if sameCount: 
            return False
        
        """
        edge case: "RL", "LR"
        """
        s, e = 0, 0
        
        while e < len(end) and s < len(start):
            #end[e] = "X"
            #end[1] = "R 
            #end[2] = "L"
            # e = 2, s = 3
            #print("hello", e)
            if end[e] == "L" and start[s] == "L":
                e += 1
                s += 1
                if s < e: return False
            elif end[e] == "R" and start[s] == "R":
                s += 1
                e += 1
                if s > e: return False
            # -> e = 2, s = 1
            elif end[e] == "L" and start[s] == "R":
                return False
            elif end[e] == "R" and start[s] == "L":
                return False
            elif end[e] == "L" or end[e] == "R":
                s += 1
                
            elif end[e] == "X":
                e += 1
               
            # e = 1  
        
        return True
        
            