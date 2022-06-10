class TrieNode {
    public TrieNode[] children;
    public char val;
    public boolean isEnded;
    public List<String> currWords;
    TrieNode() {
        children = new TrieNode[26];
        isEnded = false;
        currWords = new ArrayList<>();
    }
}

class Trie {
    private TrieNode root;
    Trie() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode curr = root;
        for (char c: word.toCharArray()) {
            if (curr.children[c-'a'] == null) curr.children[c-'a'] = new TrieNode();
            curr = curr.children[c-'a'];
            curr.val = c;
        }
        curr.isEnded = true;
    }
    
    public List<Integer> getMatch(int i, String word) {
        TrieNode curr = root;
        List<Integer> possibleI = new ArrayList<>();
        for (; i < word.length(); i++) {
            char c = word.charAt(i);
            if (curr.children[c-'a'] == null) break;
            curr = curr.children[c-'a'];
            if (curr.isEnded) possibleI.add(i);
        }
        
        return possibleI;
    }
    
}


class Solution {
    String targetS;
    Trie trieTree;
    public List<String> wordBreak(String s, List<String> wordDict) {
        // can word be reused???
        // does the order of return matter?
        trieTree = new Trie();
        targetS = s;
        for (String word: wordDict) {
            trieTree.addWord(word);
        }
        
        List<String> ans = new ArrayList<>();
        dp(0, new ArrayList<>(), ans);
        //System.out.println(ans);
        //List<String> tempAns = new ArrayList<>();
        return ans;
        
    }
    
    
    public void dp(int i, List<String> slicedI, List<String> ans) {
        if (i >= targetS.length()) {
            String joined = String.join(" ", slicedI);
            ans.add(joined);
        }
        
        List<Integer> possibleI = trieTree.getMatch(i, targetS);
        for (int nxtI: possibleI) {
            slicedI.add(targetS.substring(i, nxtI+1));
            dp(nxtI+1, slicedI, ans);
            slicedI.remove(slicedI.size()-1);
        }
        
    }
    
    
}