class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        """
    runtime: o(n*m*n) -> o(n^2*m) -> o(m*logm*n*n) for each union
    space: o(n)
        """
    
        q = collections.deque()
        visited = [False]*len(strs)
        # -> [f,f,f,f]
        count = len(strs)
        # -> count = 4
        for i, string in enumerate(strs):
            # -> string = tars
            if visited[i]: continue
            q.append(string)
            visited[i] = True
            while q:
                str1 = q.popleft()
                # -> rats
                for str2i in range(i+1, len(strs)):
                    if visited[str2i]: continue
                    if str1 == strs[str2i] or self.isSimilar(str1, strs[str2i]):
                        visited[str2i] = True
                        # -> [t,t,f,f]
                        count -= 1
                        # count = 3
                        q.append(strs[str2i])
                    # -> q = {rats}
        return count           
    
    
        
        
    def isSimilar(self, s1, s2):
        countDiff = 0
        for i in zip(s1, s2):
            if i[0] != i[1]:
                countDiff+=1
                
        return countDiff == 2