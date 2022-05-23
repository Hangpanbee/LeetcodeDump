class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        OCCUPIED = 1
        VACANT = 0
        REMAINOCCUPIED = 1
        REMAINEDVACCANT = 0
        OCCUPIEDTOVACANT = 2
        VACANTTOOCCUPIED = -2
        seen = {}
        day = 0
        isReduced = False
        while day < n:
            for i, v in enumerate(cells):
                if i == 0 or i == len(cells)-1: 
                    cells[i] = OCCUPIEDTOVACANT if cells[i] == OCCUPIED else REMAINEDVACCANT
                    continue
                leftCell = cells[i-1] 
                rightCell = cells[i+1] 
                
                if leftCell >= OCCUPIED and rightCell >= OCCUPIED:
                    cells[i] = REMAINOCCUPIED if cells[i] == OCCUPIED else VACANTTOOCCUPIED
                elif leftCell <= VACANT and rightCell <= VACANT:
                    cells[i] = REMAINOCCUPIED if cells[i] == OCCUPIED else VACANTTOOCCUPIED
                else:
                    cells[i] = REMAINEDVACCANT if cells[i] == VACANT else OCCUPIEDTOVACANT
            
             
            for i, v in enumerate(cells):
                if v == OCCUPIEDTOVACANT:
                    cells[i] = VACANT
                elif v == VACANTTOOCCUPIED:
                    cells[i] = OCCUPIED
            
            day+=1
            currSeen = tuple(cells)
            if not isReduced and currSeen in seen:
                loop = day - seen[currSeen]
                #print(loop, day, seen)
                n = (n-seen[currSeen])%loop
                day = 0
                isReduced = True
                #print(n)
                
            else:
                seen[currSeen] = day
            
        return cells
                    
                