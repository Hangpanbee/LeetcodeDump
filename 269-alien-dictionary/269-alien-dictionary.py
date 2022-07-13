class AlienDictImpl:
    
    def __init__(self, words):
        self.graph = collections.defaultdict(list)
        self.words = words
        self.isValid = self.buildGraph()
        self.finalWord = []
        self.visited = {}
        
    def buildCharGraph(self, word):
        for c in word:
            if c not in self.graph: self.graph[c] = set()
        
    def buildOrder(self, word1, word2):
        self.buildCharGraph(word1)
        self.buildCharGraph(word2)
        
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                self.graph[c1].add(c2)
                return True
        if len(word1) > len(word2):
            return False
        return True
        
        
    def buildGraph(self):
        if len(self.words) == 1: self.buildCharGraph(self.words[0])
        for i in range(len(self.words)-1):
            isValid = self.buildOrder(self.words[i], self.words[i+1])
            if not isValid: return False
        
        return True
    
    def buildFinalWord(self, char):
        
        self.visited[char] = False
        # v = {a: False}
        # v = {a: F, c: F}
        
        # a c 
      
        isNxtChar = True
        for nxtChar in self.graph[char]:
            if nxtChar in self.visited:
                isNxtChar = self.visited[nxtChar]
                break
            isNotCycle = self.buildFinalWord(nxtChar)
            if not isNotCycle: return False
        self.finalWord.append(char)
        self.visited[char] = True
        # v = {a: True}
        return isNxtChar
            

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        AlienDict = AlienDictImpl(words)
        if not AlienDict.isValid: return ""
        """
        self.graph = {
            "c": ["b"],
            "b": ["a"],
            "a": []
        }
        
        """
        for char, v in AlienDict.graph.items():
            if char not in AlienDict.visited:
                isValid = AlienDict.buildFinalWord(char)

            if not isValid: return ""
        
        AlienDict.finalWord.reverse()
        return "".join(AlienDict.finalWord)
            