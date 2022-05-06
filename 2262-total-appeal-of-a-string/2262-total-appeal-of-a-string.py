class Solution:
    def appealSum(self, s: str) -> int:
        charToIndex = collections.defaultdict(list)
        index = {}
        runningSum = 0
        for i, v in enumerate(s):
            charToIndex[v].append(i)
            runningSum += len(charToIndex)
            index[v] = 0
        #print(charToIndex, runningSum)
        
        total = runningSum
        for i, v in enumerate(s):
            if (index[v]+1) < len(charToIndex[v]):
                nextRunningSum = runningSum - (charToIndex[v][index[v]+1] - charToIndex[v][index[v]])
                index[v] += 1
            else:
                nextRunningSum = runningSum - (len(s)-i)   
            total += nextRunningSum
            runningSum = nextRunningSum
        return total