class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> counter = buildFreqCounter(s);
        
        Queue<int[]> maxHeap = new PriorityQueue<>((int[] i1, int[] i2) -> (i2[0] - i1[0]));
        int bucket = (s.length()%2==0) ? s.length()/2 : s.length()/2+1;
        for (Map.Entry<Character, Integer> e: counter.entrySet()) {
            if (e.getValue() > (bucket) ) return "";
            maxHeap.add(new int[]{e.getValue(), e.getKey()});
        }
        
        StringBuilder[] organizedChar = new StringBuilder[bucket];
        for (int i = 0; i < (bucket); i++) {
            organizedChar[i] = new StringBuilder();
        }
        
        int i = 0;
        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            // aaabbcc -> a b c a b a c
            char c = (char) curr[1];
            while (curr[0] > 0) {
                if (organizedChar[i].length() == 0 ||  c != organizedChar[i].charAt(organizedChar[i].length()-1) ) {
                    organizedChar[i].append(c);
                }
                i++;
                i%=organizedChar.length;
                --curr[0];
            }
            
        }
        //System.out.println(Arrays.toString(organizedChar));
        
        for (int j = 1; j < organizedChar.length; j++) {
            organizedChar[0].append(organizedChar[j]);
        }
        
        return organizedChar[0].toString();
        
    }
    
    private Map<Character, Integer> buildFreqCounter(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        
        for (char c: s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0)+1);
        }
        
        return counter;
    }
    
}