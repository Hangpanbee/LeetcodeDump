class LFUCache {
    private HashMap<Integer, LinkedHashMap<Integer, Integer>> mapFreqToKey;
    private HashMap<Integer, Integer> mapKeyToFreq;
    private int LFUcapacity;
    private int minFreq;
    public LFUCache(int capacity) {
        mapFreqToKey = new HashMap<>();
        mapKeyToFreq = new HashMap<>();
        LFUcapacity = capacity;
        minFreq = 1;
    }
    
    public int get(int key) {
        int freq = mapKeyToFreq.getOrDefault(key, -1);
        if (freq == -1) return -1;
        //System.out.println();
        int val = mapFreqToKey.get(freq).get(key);
        mapFreqToKey.get(freq).remove(key);
        if (freq == minFreq) {
            minFreq = mapFreqToKey.get(freq).size() == 0 ? minFreq+1 : minFreq;
           
        };
        freq++;
        mapKeyToFreq.put(key, freq);
        mapFreqToKey.computeIfAbsent(freq, s -> new LinkedHashMap<>()).put(key, val);
        return val;
    }
    
    public void put(int key, int value) {
        if (LFUcapacity == 0) return;
        int freq = mapKeyToFreq.getOrDefault(key, -1);
        if (freq == -1 && mapKeyToFreq.size() == LFUcapacity) {
            LinkedHashMap removedMap = mapFreqToKey.get(minFreq);
            //System.out.println(minFreq);
            //System.out.println(mapFreqToKey);
            Object LCU = removedMap.keySet().iterator().next();
            //System.out.println(removedMap);
            removedMap.remove(LCU);
            mapKeyToFreq.remove(LCU);
            //System.out.println(removedMap);
        };
        
        if (freq > -1) {
            mapFreqToKey.get(freq).remove(key);
            if (freq == minFreq) {
                minFreq = mapFreqToKey.get(freq).size() == 0 ? minFreq+1 : minFreq;
            };
            freq++;
            mapKeyToFreq.put(key, freq);
            mapFreqToKey.computeIfAbsent(freq, s-> new LinkedHashMap<>()).put(key, value);
        } else {
            minFreq = 1;
            mapKeyToFreq.put(key, 1);
            mapFreqToKey.computeIfAbsent(1, s -> new LinkedHashMap<>()).put(key, value);
            //System.out.println(mapFreqToKey.get(1));
        }
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */