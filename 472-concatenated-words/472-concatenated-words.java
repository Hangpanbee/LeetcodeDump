class Node {
    public HashMap<Character, Node> children;
    public Character val;
    public boolean isEnded;
    public Node() {
        children = new HashMap<>();
        isEnded = false;
    }
}

class Trie {
    public Node root;
    public Trie() {
        root = new Node();
    };
    
    public void insert(String word) {
        Node curr = root;
        
        for (char letter: word.toCharArray()) {
            curr = curr.children.computeIfAbsent(letter, af -> new Node());
            curr.val = letter;
        };
        //System.out.println(word);
        //System.out.println(curr.val);
        curr.isEnded = true;
    };
    
    public List<Pair<Node, Integer>> traverse(String word, int i) {
        Node curr = root;
        List<Pair<Node, Integer>> subword = new ArrayList<>();
        for (; i < word.length() && curr != null; i++) {
            char letter = word.charAt(i);
            
            //System.out.println(word);
            //System.out.println(letter);
            //System.out.println(curr.children);
            curr = curr.children.get(letter);
            if (curr == null) {
                return subword;
            };
            if (curr.isEnded == true) {
                subword.add(new Pair<>(curr, i+1));
            };
            
        };
        return subword;
    }
}



class Solution {
    Trie tree;
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        tree = new Trie();
        
        for (String word: words){
            tree.insert(word);
        };
        
        List<String> ans = new ArrayList<>();
        Set<String> uniqueAns = new HashSet<>();
        
        for (String word: words) {
            boolean isConcatWord = dfs(word, 0, tree.root, 0);
            if (isConcatWord == true) {
                ans.add(word);
            };
        }
        
        return ans;
        
    }
    
    
    private boolean dfs(String word, int i, Node curr, int count) {
        
        if (i == word.length() && count >= 2) {
            return true;
        } else if (i >= word.length()) {
            return false;
        }
        
        List<Pair<Node, Integer>> subwords = tree.traverse(word, i);
        //System.out.println(word);
        //System.out.println(i);
        //System.out.println(word);
        for (int j = 0; j < subwords.size(); j++) {
            Pair<Node, Integer> subword = subwords.get(j);
            //System.out.println(subword.getKey().val);
            //System.out.println(subword.getValue());
            if (dfs(word, subword.getValue(), subword.getKey(), count+1) == true) {
                return true;
            }
        }
        return false;
        
        
    }
}