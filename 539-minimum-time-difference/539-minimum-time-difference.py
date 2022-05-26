import numpy as np
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        totalMins = 24*60
        
        
        """
        [00:03, 3:03, 13:05] -> [3,  12*60+5] -> [12*60+1, 24*60+3]
        [00:00, 11:59]
        [24:00]
        """
        toInt = lambda x: int(x)
        
        zeroTP = []
        twentyFrTP = []
        for i, timepoint in enumerate(timePoints):
            H, M = timepoint.split(":")
            H = toInt(H)
            M = toInt(M)
            if H < 12:
                twentyFrTP.append((H+24)*60+M)
            else:
                twentyFrTP.append(H*60+M)
            zeroTP.append(H*60+M)      
            
        zeroTP.sort()
        twentyFrTP.sort()
        
        getMinZeroTP = np.diff(zeroTP)
        getMinTwentyTP = np.diff(twentyFrTP)
        
        return min(min(getMinZeroTP), min(getMinTwentyTP))
        