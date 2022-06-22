class Solution {
    public int[] findBuildings(int[] heights) {
        
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        List<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < heights.length; i++) {
            while (!stack.isEmpty() && heights[stack.peekLast()] <= heights[i]) {
                stack.pollLast();
            }
            // i = 0;
            // i = 1
            // i = 2
            // i = 3
            // stack = [0]
            stack.add(i);
            // stack = [0]
            // stack = [0,1]
            // stack = [0,2]
            
        }
        
        int[] oceanBuildings = new int[stack.size()];
        
        for (int i = 0; i < oceanBuildings.length; i++) {
            oceanBuildings[i]=stack.pollFirst();
        }
        
        return oceanBuildings;
        
    }
}