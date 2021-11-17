class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        #cyclic sort
        
        string1 = list(s1)
        string2 = list(s2)
        letterTracker = collections.defaultdict(list)
        
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                letterTracker[string2[i]].append(i)
        #print(letterTracker)       
        
        self.move = 999999
        
        def backtracking(string1, string2, currIndex, minMove):
            if string1 == string2:

                self.move = min(minMove, self.move)
                return
            
            if string1[currIndex] == string2[currIndex]:
                backtracking(string1, string2, currIndex+1, minMove)
            
            else:
                #if
                
                for choice in letterTracker[string1[currIndex]]:
                    if string1[choice] == string2[choice]: continue
                    #swap
                    string1[currIndex], string1[choice] = string1[choice], string1[currIndex]
                    #print(string1)
                    #backtracking
                    backtracking(string1, string2, currIndex, minMove+1)
                        
                    
                    #unswap
                    string1[currIndex], string1[choice] = string1[choice], string1[currIndex]

        
        backtracking(string1, string2, 0, 0)
  
                
        
        
        

        return self.move if self.move != 9999999 else 0
                
                
        
        