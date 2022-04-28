class Solution {
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        PriorityQueue<nodePath> q = new PriorityQueue<>((n1, n2) -> n1.maxDiff - n2.maxDiff);
        nodePath node = new nodePath(0, 0, 0);
        q.add(node);
        HashSet<Pair<Integer, Integer>> visited = new HashSet<>();
        visited.add(new Pair<Integer, Integer> (0, 0));
        int dirs[][] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            nodePath curr = q.poll();

            if (curr.r == m-1 && curr.c == n-1) return curr.maxDiff; 
            visited.add(new Pair<Integer, Integer> (curr.r, curr.c));
            for (int[] x: dirs) {
                int newR = curr.r + x[0];
                int newC = curr.c + x[1];
                
                if ((newR < 0) || (newR >= m) || (newC < 0) || (newC >= n)) continue;
                Pair<Integer, Integer> newRC = new Pair(newR, newC);
                if (visited.contains(newRC)) continue;
                
                int currMaxDiff = heights[newR][newC] - heights[curr.r][curr.c];
                nodePath nextPath = new nodePath(Math.max(Math.abs(heights[newR][newC] - heights[curr.r][curr.c]), curr.maxDiff), newR, newC);
                
                q.add(nextPath);
            }
            
        };
        
        return -1;   
    }
}

class nodePath{
    int maxDiff;
    int r;
    int c;
    public nodePath(int maxDiff, int r, int c) {
        this.maxDiff = maxDiff;
        this.r = r;
        this.c = c;
    };
    

} 