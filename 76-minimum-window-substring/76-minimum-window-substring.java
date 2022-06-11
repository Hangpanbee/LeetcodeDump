class Solution {
    public String minWindow(String s, String t) {
        // a  d  o  b  e  c o d e b a n c
        //a0  1  2  3  4  5 4 3 2 1 0 1 2
        //a                         0 1 2
        //b99 99 99 0  1  2 3 4 5 0 1 2 3
        //c99 99 99 99 99 0 1 2 3 4 5 6 0
        //20 20 20  20 20 7 101315136 9 5 
        HashMap<Character, Integer> mapCharToFreq = new HashMap<>();
        for (char c: t.toCharArray()) {
            mapCharToFreq.put(c, mapCharToFreq.getOrDefault(c, 0)+1);
        }
        //ADOBECBANC
        int tLen = mapCharToFreq.size();
        int l = 0; int r = 0;
        Pair<Integer, Integer> targetIndex = new Pair<>(-1, -1);
        while (r < s.length()) {
            char currRC = s.charAt(r);
            if (mapCharToFreq.containsKey(currRC)) {
                mapCharToFreq.put(currRC, mapCharToFreq.get(currRC)-1);
                if (mapCharToFreq.get(currRC) == 0) tLen--;
            }
            //System.out.println(mapCharToFreq);
            //System.out.println(tLen);
            while (tLen == 0) {
                char currLC = s.charAt(l);
                if (mapCharToFreq.containsKey(currLC)) {
                    if ((targetIndex.getValue() - targetIndex.getKey()) >= (r-l) || targetIndex.getValue() == -1) {
                        targetIndex = new Pair<>(l, r);
                    }
                    mapCharToFreq.put(currLC, mapCharToFreq.get(currLC)+1);
                    if (mapCharToFreq.get(currLC) > 0) tLen++;
                }
                l++;
            }
            
            
            r++;
        }
        
        //System.out.println(targetIndex);
        if (targetIndex.getKey() == -1 && targetIndex.getValue() == -1) return "";
        else return s.substring(targetIndex.getKey(), targetIndex.getValue()+1);
        
        
    }
}