class TrieNode:
    def __init__(self, val = "", children = {}):
        self.val = val
        self.children = {}
        self.hot = []
        
class Trie: 
    def __init__(self):
        self.root = TrieNode()
        
        
    def add(self, sentence):
        # [("i love you", 5), ("island", 3), ("ironman", 2), ("i love leetcode", 2)]
        
        for i, sentence in enumerate(sentence):
            curr = self.root
            w = sentence
            for j, ch in enumerate(w):
                if ch not in curr.children:
                    curr.children[ch] = TrieNode(ch, {})
                curr = curr.children[ch]
                curr.hot.append(w)
    

    def get(self, input, currNode):
        
        if input in currNode.children:
            return (currNode.children[input].hot, currNode.children[input])
        else:
            return ([], TrieNode())
        
        
        
    

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.Trie = Trie()
        self.mapStoC = {}
        for i in range(len(sentences)):
            self.mapStoC[sentences[i]] = times[i]
        self.Trie.add(sentences)
        self.currNode = self.Trie.root
        self.currSentence = []

    def input(self, c: str) -> List[str]:
        if c == "#": 
            self.currNode = self.Trie.root
            joinedSentence = "".join(self.currSentence)
            if joinedSentence not in self.mapStoC:
                self.mapStoC[joinedSentence] = 1
                self.Trie.add([joinedSentence])
            else: 
                self.mapStoC[joinedSentence] += 1
            self.currSentence = []
            return []
        self.currSentence.append(c)
        matchedWords, self.currNode = self.Trie.get(c, self.currNode)
        matchedWords = self.__getHot(matchedWords)
        
        return matchedWords

    
    def __getHot(self, hotSentences):

        hotSentences.sort(key = lambda x: (-self.mapStoC[x], x))
        
        return hotSentences[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)