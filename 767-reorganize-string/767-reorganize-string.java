class Solution {
    public String reorganizeString(String s) {
        
        Queue<int[]> maxHeap = new PriorityQueue<>(
            (int[] p1, int[] p2) -> p2[1] - p1[1]
        );
           
        Map<Character, Integer> mapCharToFreq = getCounter(s);    
            
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            maxHeap.add(new int[]{e.getKey(), e.getValue()});
        }
        
        // aab
        StringBuilder ans = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            int[] first = maxHeap.poll();
            // first [a, 2]
            // first [a, 1]
            if (ans.length() == 0 || ans.charAt(ans.length()-1) != (char) first[0]) {
                ans.append((char) first[0]);
                // ans = 'a'
                first[1]--;
                // first [a, 1]
                if (first[1] > 0) {
                    maxHeap.add(first);
                    // maxHeap = [(a, 1), (b, 1)]
                }
            } else {
                if (maxHeap.isEmpty()) return "";
                int[] scnd = maxHeap.poll();
                // scnd = ['b', 1]
                ans.append((char) scnd[0]);
                // ans = 'ab'
                scnd[1]--;
                
                if (scnd[1] > 0) {
                    maxHeap.add(scnd);
                }
                maxHeap.add(first);
                
            }
            
        }

        if (ans.length() < s.length()) return "";
        else return ans.toString();
        
    }
    
    private Map<Character, Integer> getCounter(String s) {
        Map<Character, Integer> mapCharToFreq = new HashMap<>();
        
        for (char c: s.toCharArray()) {
            mapCharToFreq.put(c, mapCharToFreq.getOrDefault(c, 0)+1);
        }
        
        return mapCharToFreq;
    }
}