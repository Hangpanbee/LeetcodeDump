class UnionFind:
    def __init__(self, size):
        # self root shows that the parent of a node is itself
        self.root = list(range(size + 1))
        self.group = size
        # each component is of size 1
        self.size = [1] * (size + 1)
    
    # path compression
    # find root node of p
    def find(self, p):
        if p == self.root[p]:
            return p
        self.root[p] = self.find(self.root[p])
        return self.root[p]
        
    def union(self, e1, e2):
        roote1 = self.find(e1)
        roote2 = self.find(e2)
        roote1size = self.size[roote1]
        roote2size = self.size[roote2]
        
        if roote1 != roote2:
            if roote1size >= roote2size:
                self.root[roote2] = roote1
            else:
                self.root[roote1] = roote2
                
            self.size[roote2] = self.size[roote1] = roote1size + roote2size
            self.group -= 1
            return True
        return False
            
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        res = 0
        #classic union find problem
        AliceTracker = UnionFind(n)
        BobTracker = UnionFind(n)
        
        for edgeType, e1, e2 in edges:

            if edgeType == 3:
                # if it is not in the same union
                a = AliceTracker.union(e1, e2)
                b = BobTracker.union(e1, e2)
                if a and b: res += 1
            else: continue
               

        for edgeType, e1, e2 in edges:
            if edgeType == 1:
                
                if AliceTracker.union(e1, e2):
                    res += 1
            elif edgeType == 2:
                if BobTracker.union(e1, e2):
                    res += 1

        return len(edges)-res if AliceTracker.group == 1 and BobTracker.group == 1 else -1
        
        