class UnionFind {
    int[] root;
    int[] rank;
    int groups;
    public UnionFind(int comp) {
        root = new int[comp];
        rank = new int[comp];
        groups = comp;
        Arrays.fill(rank, 1);
        for (int i = 0; i < comp; i++) {
            root[i] = i;
        };
    
    }
    
    public int find(int c) {
        while (root[c] != c) {
            c = root[c];
        };
        return c;
    }
    
    public boolean union(int c1, int c2) {
        int c1Parent = find(c1);
        int c2Parent = find(c2);
        int c1Rank = rank[c1Parent];
        int c2Rank = rank[c2Parent];

        if (c1Parent == c2Parent) return false;
        if (c1Rank >= c2Rank) {
            root[c2Parent] = c1Parent;
            rank[c1Parent] += rank[c2Parent];
        } else {
            root[c1Parent] = c2Parent;
            rank[c2Parent] += rank[c1Parent];
        };
        groups--;
        return true;
        
    }
    
    
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
       int cables = connections.length;
       UnionFind UF = new UnionFind(n);
       int extraCables = 0;
       for (int[] connection : connections) {
           boolean isNeeded = UF.union(connection[0], connection[1]);
           if (isNeeded == false) {
                extraCables += 1; 
           };
       };
        //System.out.println(UF.groups);
        int numDisconnected = UF.groups - 1;
        return numDisconnected <= extraCables ? numDisconnected : -1;
        
        
    }
}