class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        
        m = 10**9+7
        
        phone = {0:[4, 6], 1:[6, 8], 2:[7, 9], 3: [4, 8], 4:[0, 3, 9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        nxtStateFreq = [2,2,2,2,3,0,3,2,2,2]
        
        for i in range(2, n):
            currState = nxtStateFreq
            nxtStateFreq = [0]*10
            for k, v in phone.items():
                for nxtNum in v:
                    nxtStateFreq[nxtNum] += currState[k]

        
        #print(currState, nxtStateFreq)
        return sum(nxtStateFreq)%m
            
        