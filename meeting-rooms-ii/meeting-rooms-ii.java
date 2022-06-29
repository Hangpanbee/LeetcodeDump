class Solution {
    public int minMeetingRooms(int[][] intervals) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        
        for (int[] interval: intervals) {
            int start = interval[0];
            int end = interval[1];
            map.put(start, map.getOrDefault(start, 0)+1);
            map.put(end, map.getOrDefault(end, 0)-1);
            
        };
        
        int runningSum = 0;
        int ans = -1;    
        for (Map.Entry<Integer, Integer> mapEntry : map.entrySet() ) {
            runningSum += mapEntry.getValue();
            ans = Math.max(ans, runningSum);
        };
        
        return ans;
        
        
    }
}