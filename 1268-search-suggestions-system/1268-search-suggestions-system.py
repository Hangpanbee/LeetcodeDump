class TrieNode:
    def __init__(self, val=""):
        self.val = ""
        self.matchingStrings = []
        self.children = {}
        self.isEnded = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s1):
        curr = self.root
        for i, v in enumerate(s1):
            if v not in curr.children:
                curr.children[v] = TrieNode(v)
            curr = curr.children[v]
            curr.matchingStrings.append(s1)
        
        curr.isEnded = True
                
        
    def getMatchingStrings(self, s1):
        curr = self.root
        allMatchingStrings = []
        for i,v in enumerate(s1):
            #print(curr.matchingStrings[:3])
            if v not in curr.children: 
                allMatchingStrings.extend([] for i in range(len(s1)-i))
                return allMatchingStrings
            curr = curr.children[v]
            allMatchingStrings.append(curr.matchingStrings[:3])
      
           
        return allMatchingStrings
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        """
        runtime:
            - Trie: insert, get: o(k) where k is the arbitrary length of the input string
            --> totalInsert = o(n*k) where n is the length of products and k is the length of string
            - sort products: o(nlogn + n*k) -> o(nlogn)
        space:
            - Trie: o(k) where k is the arbitrary length of the longest input string
            -> o(26) is round down to o(1)
        """
        """
        1. initiate the trie tree
        2. insert products to trie
        3. call getMachingStrings to get all matching products at each level
        """
        products.sort()
        
        productsTrie = Trie()
        for i, product in enumerate(products):
            productsTrie.insert(product)
        
        
        allMatchingStrings = productsTrie.getMatchingStrings(searchWord)
        
        return allMatchingStrings
            
        
        
        
        
        