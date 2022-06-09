class Dictionary {
    Map<Character, List<Character>> graph;
    boolean[] visited;
    boolean[] visiting;
    List<Character> alienWord;
    Dictionary() {
        graph = new HashMap<>();
        visited = new boolean[26];
        Arrays.fill(visited, false);
        visiting = new boolean[26];
        Arrays.fill(visiting, false);
        alienWord = new ArrayList<>(); 
    };
    
    private void getCharToGraph(String word) {
        for (char c: word.toCharArray()) {
            graph.computeIfAbsent(c, s -> new ArrayList<Character>());
        }
        
    }
    
    public boolean buildGraph(String[] words) {
        getCharToGraph(words[0]);
        for (int i = 0; i < (words.length-1); i++) {
            boolean isValid = buildDependency(words[i], words[i+1]);
            if (!isValid) return false;
        }
        return true;
        
    }
    
    private boolean buildDependency(String word1, String word2) {
        getCharToGraph(word1);
        getCharToGraph(word2);
        for (int i = 0; i < Math.min(word1.length(), word2.length()); i++) {
            char c1 = word1.charAt(i);
            char c2 = word2.charAt(i);
            if (c1 != c2) {
                graph.get(c2).add(c1);
                return true;
            }
        }
        if (word1.length() > word2.length()) {
            return false;
        } 
        return true;
        
    }
    
    public boolean buildAlienString(Character c) {
        
        visiting[c-'a'] = true;
        for (char nxtC: graph.get(c)) {
            if (visiting[nxtC - 'a']) return false;
            
            if (!visited[nxtC - 'a']) {
                boolean isCycle = buildAlienString(nxtC);
                if (!isCycle) return false;
            }   
        }
        // r -> e -> w -> alienWord = [w,e,r,t]
        visiting[c-'a'] = false;
        if (!visited[c-'a']) alienWord.add(c);
        visited[c-'a'] = true;
        
        return true;
    }
    

    //ftrew,     
}


class Solution {
    public String alienOrder(String[] words) {
        Dictionary dict = new Dictionary();
        boolean isValid = dict.buildGraph(words);
        if (!isValid) return "";
        //System.out.println(dict.graph);
        for (Map.Entry<Character, List<Character>> e: dict.graph.entrySet()) {
            isValid = dict.buildAlienString(e.getKey());
            if (!isValid) return "";
        }
        
        StringBuilder sb = new StringBuilder();
        for (Character c: dict.alienWord) {
            sb.append(c);
        }
        
        return sb.toString();
    }
}