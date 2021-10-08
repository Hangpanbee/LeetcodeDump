class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(currSum, result, results, candidates):
            #print(candidates, result, currSum)
            if currSum == 0: 
                results.append(result)
                return
            elif not candidates or currSum < candidates[0]: 
                return
            
            #should we start with 0?
            n = 0
            while (n*candidates[0]) <= currSum:
                leftover = currSum - (candidates[0]*n)
                helper(leftover, result + [candidates[0]]*n, results, candidates[1:])
                n+=1
            return
            

        candidates.sort()
        results = []

        for choice in range(len(candidates)):
            result = [candidates[choice]]
            helper(target-candidates[choice], result, results, candidates[choice:])
            
        
        
        
        return results
            #ending condition: if currSum/leftover == 0: results.append(result)
            # else currSum < candidates[0]: return
            
            #while n * candidate < currSum:
                #result.extend([candidate]*n)
                #leftover = result - (candidate*n)
                #recurse: helper(currSum = leftover, result + [[candidiate]*n], results, candidates[1::])
                #backtrack: 
                #n += 1
            #return 
        
        
        #candidates = [2,3,6,7]
        #first call: candidates [2,3,6,7]
        #second call: candidates [3,6,7], leftover/currSum = 5
        #third call: candidates [6,7], leftover = 5
        # --> first call: n = 2 leftover = 3
        # --> second call: candidates [3,6,7], leftover = 0