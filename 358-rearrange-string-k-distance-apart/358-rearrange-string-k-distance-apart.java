class Solution {
    public String rearrangeString(String s, int k) {
        if (k == 0) return s;
        Map<Character, Integer> mapCharToFreq = buildCounter(s);
        
        if (mapCharToFreq.size() < k) return "";
        
        // aaaabbccdd -> a b c a b d a d c a
        // a:1, b:1, c:1, d:1
        // [acd] [adc] [ab] [ba]
        // aaaaddbbcc -> a: 1, b: 1, c:1 k = 2
        // [abc] [abc] [abd] [ac]
        // [a] [a] [a] [a]
        int bucketCount = s.length()%k == 0 ? (s.length()/k) : (s.length()/k+1);
        StringBuilder[] bucket = new StringBuilder[bucketCount];
        Queue<int[]> maxHeap = new PriorityQueue<>((int[] i1, int[] i2) -> i2[0] - i1[0]);
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            if (e.getValue() > bucketCount) return "";
            maxHeap.add(new int[]{e.getValue(), e.getKey()});
        }
        
        for (int i = 0; i < bucketCount; i++) {
            bucket[i] = new StringBuilder();
        }
        // {a: 3, b: 2, c: 1, e: 1}
        // [ab] [ab] [a]
        int i = 0;
        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            // curr = [3, a]
            char c = (char) curr[1];
            
            while (curr[0] > 0) {
                if (bucket[0].length() == 0 ||
                    i == (bucketCount-1) && bucket[0].charAt(bucket[0].length()-1) != c) {
                    i = 0;
                }                 
                bucket[i].append(c);
                //[ab] [ab] [a]
                i++;
                i%=bucketCount;
                curr[0]--;
            }
            
        }
        //System.out.println(Arrays.toString(bucket));
        for (int j = 0; j < bucketCount; j++) {
            if (j < (bucketCount-1) && bucket[j].length() < k) return "";
            if (j==0) continue;
            bucket[0].append(bucket[j]);
        }
        
        return bucket[0].toString();
    }
    
    private Map<Character, Integer> buildCounter(String s) {
        Map<Character, Integer> mapCharToFreq = new HashMap<>();
        for (char c: s.toCharArray()) {
            mapCharToFreq.put(c, mapCharToFreq.getOrDefault(c, 0)+1);
        }
        
        return mapCharToFreq;
    }
}