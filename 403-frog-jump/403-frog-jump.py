class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        
        sQ, eQ = collections.deque(), collections.deque()
        sV, eV = {}, {(stones[-1]-stones[-2], stones[-1]): True}
        sQ.append((0, 0))
        eQ.append((stones[-1], stones[-1] - stones[-2]))
        GOAL = stones[-1]
        
        while sQ and eQ:
            pos, units = sQ.popleft()
            #print(pos, units)
            #print(sV, eV)
            for nextUnits in [(units+1), (units), (units-1)]:
                nextPos = pos + nextUnits
                #print(nextPos in stones, sV, nextUnits)
                if (nextUnits, nextPos) in sV: continue
                if (nextPos) in stones and  0 <= pos < (pos+nextUnits) :
                    sQ.append((pos+nextUnits, nextUnits))
                    if nextPos == GOAL: return True
                    if (nextUnits, nextPos) in eV: return True
                    sV[(nextUnits, nextPos)] = True              
                    
            rPos, rUnits = eQ.popleft()
            for nextRUnits in [(rUnits+1), (rUnits), (rUnits-1)]:
                nextRPos = rPos - nextRUnits
                if (nextRUnits, nextRPos) in eV: continue
                if nextRPos >= 0 and nextRPos in stones:
                    eQ.append((nextRPos, nextRUnits))
                    if (nextRUnits, nextRPos) in sV: return True
                    eV[(nextRUnits, nextRPos)] = True
            
        #print(eV, sV) 
        return False
        
        