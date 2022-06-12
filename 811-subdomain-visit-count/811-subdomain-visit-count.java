class TrieNode {
    public String domain;
    public Map<String, TrieNode> children;
    public int count;
    TrieNode(String domain, int count) {
        this.domain = domain;
        children = new HashMap<>();
        this.count = count;
    }
}

class Trie {
    TrieNode root;
    Trie() {
        root = new TrieNode("", 0);
    }
    
    public void insert(String[] words, int count) {
        TrieNode currRoot = root;
        
        for (int i = words.length-1; i > -1; i--) {
            String currW = words[i];
            if (currRoot.children.containsKey(currW)) {
                currRoot.children.get(currW).count += count;
            } else {
                if (currRoot.domain == "") {
                  currRoot.children.put(currW, new TrieNode(currW, count));  
                }
                else currRoot.children.put(currW, new TrieNode(currW+"."+currRoot.domain, count));
            }
            
            currRoot = currRoot.children.get(currW);
        }
        
    }
    
    public List<String> traverse() {
        List<String> ans = new ArrayList<>();
        TrieNode currRoot = root;
        traverse(currRoot, ans);
        return ans;
    }
    
    public void traverse(TrieNode root, List<String> nodeVals) {
        if(root != this.root) nodeVals.add(Integer.toString(root.count) + " " + root.domain);
        for (Map.Entry<String, TrieNode> nxtRoot: root.children.entrySet()) {
            traverse(nxtRoot.getValue(), nodeVals);
        }
    }
    
}

class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        // count - paired domains
        // in any order
        // subdomains vs doamins
        // dicuss.now.leetcode.com
        // what if collisions??? is the cpdomains unique?
        //      com
        //        /   \
        //   mail
        //  /   \
        // intel google   
        // /   \
        //dev           
        Trie trieTree = new Trie();           
        for (String domain: cpdomains) {
            String[] pairsSplit = domain.split(" ");
            int count = Integer.parseInt(pairsSplit[0]);
            String[] domainSplit = pairsSplit[1].split("\\.");
            trieTree.insert(domainSplit, count);
        }
        //System.out.println(trieTree.root.domain);
        
        return trieTree.traverse();
                  
    }
    

}