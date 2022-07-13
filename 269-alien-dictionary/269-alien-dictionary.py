class dictGraph:
    def __init__(self):
        self.graphRep = collections.defaultdict(set)
        self.seen = {}
        self.orderedOutput = []

        
    def buildGraph(self, words):
        if len(words) == 1: self.getCharToGraph(words[0])
        for i in range(len(words)-1):
            #print(words[i], words[i+1])
            isValid = self.addWordToGraph(words[i], words[i+1])
            if not isValid: return {}
        return True
            
    def getCharToGraph(self, w):
        #print(w)
        for ch in w:
            if ch not in self.graphRep:
                self.graphRep[ch] = set()
    
    
    def addWordToGraph(self, w1, w2):
        self.getCharToGraph(w1)
        self.getCharToGraph(w2)
        for i in zip(w1, w2):
            if i[0] != i[1]:
                self.graphRep[i[0]].add(i[1])
                return True

        if len(w1) > len(w2):
            return False
        return True

    def dfs(self, node):
        
        if node in self.seen:
            return self.seen[node]
        self.seen[node] = False
        for nxtNode in self.graphRep[node]:
            isCycle = self.dfs(nxtNode)
            #print(isCycle, node)
            if not isCycle: return False
        
        self.orderedOutput.append(node)
        self.seen[node] = True
        return self.seen[node]
        

class Solution:
    def alienOrder(self, words: List[str]) -> str:
   
        
        DG = dictGraph()
        isValid = DG.buildGraph(words)
        #print(isValid, DG.graphRep)
        if not isValid: return ""
        #print(DG.graphRep)
        
        for k, v in DG.graphRep.items():
            
            
            isCycle = DG.dfs(k)
                
            if not isCycle: return ""
                
        DG.orderedOutput.reverse()
        return "".join(DG.orderedOutput)
        
