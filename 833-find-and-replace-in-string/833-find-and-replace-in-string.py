class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        prefixRange = [0]*len(s)
        appendRange = ['']*len(s)
        """
            [a b c d]
            [2,0,1,-1]
            [eee,]
        """
        
        
        for i in range(len(indices)):
            indice = indices[i]
            source = sources[i]
            target = targets[i]
            if s[indice: indice+len(source)] == source:
                if len(source) == 1: prefixRange[i] = 2
                else:
                    prefixRange[indice] = 1
                    prefixRange[indice+len(source)-1] = -1
                appendRange[indice] = target
        
        replacedString = []
        runningSum = 0
        for i in range(len(prefixRange)):
            if prefixRange[i] == 2:
                replacedString.append(appendRange[i])
            elif prefixRange[i] == 1:
                replacedString.append(appendRange[i])
                runningSum += 1
            elif prefixRange[i] == -1:
                runningSum -= 1
            elif prefixRange[i] == 0 and runningSum == 0:
                replacedString.append(s[i])            

            
            
        return "".join(replacedString)
        
        
        
        