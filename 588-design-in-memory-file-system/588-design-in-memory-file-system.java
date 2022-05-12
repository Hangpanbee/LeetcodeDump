class TrieNode {
    public StringBuilder content;
    public TreeMap<String, TrieNode> children;
    public String fileName;
    public boolean isDirectory;
    public TrieNode(String fileName, String content) {
        this.fileName = fileName;
        this.content = new StringBuilder();
        this.content.append(content);
        this.isDirectory = false;
    };
    public TrieNode(String fileName, TreeMap children) {
        this.fileName = fileName;
        this.children = children;
        this.isDirectory = true;
    };
    public TrieNode() {};
    
};

class Trie {
    private TrieNode root;
    Trie() {
        root = new TrieNode();
        root.fileName = "root";
        root.isDirectory = true;
        root.children = new TreeMap<String, TrieNode>();
    }
    
    public void create(String path) {
        String[] pathSplit = path.split("/");
        Pair<TrieNode, Integer> pair = traverse(pathSplit);
        int i = pair.getValue();
        TrieNode curr = pair.getKey();
        
        for (; i < pathSplit.length; i++) {
            TrieNode nextNode = new TrieNode(pathSplit[i], new TreeMap<String, TrieNode>());
            curr.children.put(pathSplit[i], nextNode);
            curr = nextNode;
        };        
        //System.out.println(curr.fileName);
    };
    
    public void create(String path, String content) {
        String[] pathSplit = path.split("/");
        Pair<TrieNode, Integer> pair = traverse(pathSplit);
        TrieNode curr = pair.getKey();
        int i = pair.getValue();
        if (curr.isDirectory) {
            curr.children.put(pathSplit[i], new TrieNode(pathSplit[i], content));
        } else {
            curr.content.append(content);
        };
    };
    
    public Pair<TrieNode, Integer> traverse(String[] pathSplit) {
        //System.out.println(Arrays.asList(pathSplit).toString());
        TrieNode curr = root;
        List<TrieNode> ans = new ArrayList<>();
        int i = 1;
        for (; i < pathSplit.length; i++) {
            if (curr.children == null || curr.children.get(pathSplit[i]) == null) {
                return new Pair<TrieNode, Integer>(curr, i); 
            };
            curr = curr.children.get(pathSplit[i]);
        };
        //System.out.println(i);
        return new Pair<TrieNode, Integer> (curr, i);
    };
    
    
};



class FileSystem {
    private Trie root;
    public FileSystem() {
        root = new Trie();
    }
    
    public List<String> ls(String path) {
        //if (path.equals("/")) return new ArrayList<String>();
        List<String> ans = new ArrayList<String>();
        String[] pathSplit = path.split("/");
        Pair<TrieNode, Integer> pair = root.traverse(pathSplit);
        TrieNode curr = pair.getKey();
        if (curr.isDirectory) {
            for (Map.Entry<String, TrieNode> entry: curr.children.entrySet()) {
                ans.add(entry.getKey());
                
            };
            //Collections.sort(ans);
        } else {
            ans.add(curr.fileName);
        };
        
        
        return ans;
    }
    
    public void mkdir(String path) {
        root.create(path);
    }
    
    public void addContentToFile(String filePath, String content) {
        root.create(filePath, content);
    }
    
    public String readContentFromFile(String filePath) {
        String[] pathSplit = filePath.split("/");
        Pair<TrieNode, Integer> pair = root.traverse(pathSplit);
        
        return pair.getKey().content.toString();
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * List<String> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * String param_4 = obj.readContentFromFile(filePath);
 */