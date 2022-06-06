class Solution {
    public boolean leadsToDestination(int n, int[][] edges, int source, int destination) {
     

        
        HashMap<Integer, List<Integer>> graph = new HashMap();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<Integer>());
        }
        
        for (int[] edge : edges) {
           
            graph.get(edge[0]).add(edge[1]);
        }
        //System.out.println(graph);
        
        boolean ans = dfs(graph, source, new HashSet<Integer>(), destination);
        //System.out.println(ans);
        
        return ans;
        
    }
    
    public boolean dfs(HashMap<Integer, List<Integer>> graph, int start, HashSet<Integer> visited, int destination) {
        if (start == destination && graph.get(destination).size() > 0) {
            return false;
        }
        else if (start == destination) {
            return true;
        }
        
        Boolean isReachable = null;
        for (int nxtNode: graph.get(start)) {
            if (!visited.contains(nxtNode)) {
                visited.add(nxtNode);
                if (isReachable == null) isReachable = true;
                isReachable = isReachable && dfs(graph, nxtNode, visited, destination);
                visited.remove(nxtNode);
            } else {
                isReachable = false;
            }
        };
        //System.out.println(isReachable);
        return isReachable == null ? false : isReachable;
        
    }
}