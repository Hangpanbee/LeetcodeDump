class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        questions: are the numbers always positive?
        
        """
        if firstLen < secondLen:
            firstLen, secondLen = secondLen, firstLen
      
        # -> firstLen = 2, secondlen = 1
        def getSumTwo(nums):      
            prefixSum = [0]*(len(nums)+1)
            # -> prefixSum = [0,0,0,0,0,0,0,0,0]
            scndSum = [0]*(len(nums)+1)
            # -> prefixSum = [0,0,0,0,0,0,0,0,0]
            runningSum = 0
            # -> runningSum = 0
            maxAns = 0
            # -> maxAns = 0
            for i, num in enumerate(nums):
                runningSum += num
                # -> runningSum = 6
                # -> runningSum = 11
                prefixSum[i+1] = runningSum
                if (i+1) >= secondLen:
                    scndSum[i+1] = max(scndSum[i], prefixSum[i+1]-prefixSum[i+1-secondLen])
                
                if (i+1) >= (firstLen+secondLen):
                    currSum = (prefixSum[i+1] - prefixSum[i-firstLen+1]) + scndSum[i-firstLen+1]
                    maxAns = max(currSum, maxAns)
            #print(scndSum, prefixSum)
            return maxAns
        
        left, right = getSumTwo(nums), getSumTwo(nums[::-1])
        #print(left, right)
        return max(left, right)
                 
    