class TrieNode:
    def __init__(self, letter: str):
        self.letter: str = letter
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_word: bool = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode('')
        
    def add(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
                
            node = node.children[c]
            node.count += 1
            
        node.is_word = True
        return self
    
    def _search_prefix(self, prefix) -> Optional[TrieNode]:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return self.root
            
            node = node.children[c]
            
        return node
    
    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node.is_word
        
    def search_prefix(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node != self.root
    
    def remove(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                return
            
            child = node.children[c]
            child.count -= 1
            if child.count == 0:
                del node.children[c]
                return
            
            node = child
            
        node.is_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        
        trie = Trie()
        for word in words:
            trie.add(word)            
           
        found_words = []
        for i in range(n):
            for j in range(m):
                letter = board[i][j]
                if not trie.search_prefix(letter):
                    continue
                    
                visited = set()
                visited.add((i, j))
                
                queue = deque()
                queue.append((i, j, letter, visited))
                             
                while len(queue) > 0:
                    x, y, prefix, visited = queue.popleft()
                    if trie.search(prefix):
                        found_words.append(prefix)
                        trie.remove(prefix)
                             
                    for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited:
                            if trie.search_prefix(prefix + board[dx][dy]):
                                visited_copy = visited.copy()
                                visited_copy.add((dx, dy))
                                queue.append((dx, dy, prefix + board[dx][dy], visited_copy))     
                
        return found_words