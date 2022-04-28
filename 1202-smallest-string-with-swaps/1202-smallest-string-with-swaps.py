class DisjointSet:
    
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, l1, l2):
        parentL1 = self.find(l1)
        parentL2 = self.find(l2)
        
        
        #this part is very important!
        if self.rank[parentL1] > self.rank[parentL2]:
            self.parent[parentL2] = self.parent[parentL1]
            self.rank[parentL2] += self.rank[parentL1]
            return self.parent[parentL2]
        elif self.rank[parentL1] < self.rank[parentL2]:
            self.parent[parentL1] = self.parent[parentL2]
            self.rank[parentL1] += self.rank[parentL2]
            return self.parent[parentL1]
        else:
            self.parent[parentL2] = self.parent[parentL1]
            self.rank[parentL2] += self.rank[parentL1]
            
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        if not pairs: return s
        
        
        #initiate variables
        disjointSet = DisjointSet(len(s))
        sList = list(s)
        
        for pair1, pair2 in pairs:
            currParent = disjointSet.union(pair1, pair2)
         
      
        mapIndexToLetter = collections.defaultdict(list)
        for i in range(len(s)):
            parent = disjointSet.find(i)
            heapq.heappush(mapIndexToLetter[parent], sList[i])


        ans = ""
        for i in range(len(s)):
            parent = disjointSet.find(i)
            ans += heapq.heappop(mapIndexToLetter[parent])

        return ans
            
            
        
        
        
        
        
        
        