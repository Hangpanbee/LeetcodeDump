class TrieNode:
    def __init__(self, val = "", count = 0):
        self.val = val
        self.count = count
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = []
        
    def add(self, subdomains, sVisit):
        curr = self.root
        for sd in subdomains:
            if sd not in curr.children:
                curr.children[sd] = TrieNode(sd, 0)
            curr = curr.children[sd]
            curr.count += sVisit
            
    def traverse(self):
        self._traverse(self.root, [])
        
    def _traverse(self, node, currDomain):
        
        if node.val: 
            currDomain.append(node.val)
            self.res.append(str(node.count) + " " + ".".join(currDomain[::-1]))
   
        for k, nxtNode in node.children.items():
            self._traverse(nxtNode, currDomain.copy())

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
            ["9001 discuss.leetcode.com"] -> (9001, discuss.leetcode.com), (9001, leetcode.com), (9001 com)
        """
        
        TrieTree = Trie()
        
        for domain in cpdomains:
            count, domainName = domain.split(" ")
            count = int(count)
            subdomains = domainName.split(".")
            subdomains.reverse()
            TrieTree.add(subdomains, count)
            
        TrieTree.traverse()
        return TrieTree.res