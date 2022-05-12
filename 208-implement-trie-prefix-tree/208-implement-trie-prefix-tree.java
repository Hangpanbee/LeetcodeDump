class TrieNode {
    public boolean isEnded;
    public HashMap<Character, TrieNode> children = new HashMap<>();
    public char val;
    public TrieNode(char c) {
        this.val = c;
    };
    public TrieNode() {
        
    }
}

class Trie {
    private TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode curr = root;
        
        for (int i = 0; i < word.length(); i++) {
            if (curr.children.get(word.charAt(i)) == null) {
                TrieNode nextNode = new TrieNode(word.charAt(i));
                curr.children.put(word.charAt(i), nextNode);
            };
            curr = curr.children.get(word.charAt(i));
            
        };
        curr.isEnded = true;
    }
    
    public boolean search(String word) {
        return search(word, 1);
    }
    
    public boolean startsWith(String prefix) {
        return search(prefix, 2);
    }
    
    public boolean search(String word, int type) {
        TrieNode curr = root;
        
        for (int i = 0; i < word.length(); i++) {
            if (curr.children.get(word.charAt(i)) == null) {
                return false;
            };
            curr = curr.children.get(word.charAt(i));
        };
        //System.out.println(curr.val);
        return type == 1 ? curr.isEnded: true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */