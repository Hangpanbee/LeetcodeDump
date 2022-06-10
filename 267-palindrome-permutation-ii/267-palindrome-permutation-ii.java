class Solution {
    int maxPaliRoot;
    List<String> paliRoots;
    char oddPali;
    public List<String> generatePalindromes(String s) {
        Map<Character, Integer> mapCharToFreq = buildMapCharToFreq(s);
        if (!isValidPali(mapCharToFreq)) return new ArrayList<>();
        
        maxPaliRoot = s.length()/2;
        paliRoots = new ArrayList<String>();
        oddPali = 0;
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            if (e.getValue()%2==1) {
                oddPali = e.getKey();
                mapCharToFreq.put(e.getKey(), (e.getValue()-1)/2);
            } else {
                mapCharToFreq.put(e.getKey(), e.getValue()/2);
            }
        }
        
        buildPaliRoot(mapCharToFreq, new char[maxPaliRoot], 0);
        //List<String> paliPerm = new ArrayList<>();

        
        return paliRoots;
        
        
        
    }
    
    public void buildPaliRoot(Map<Character, Integer> mapCharToFreq, char[] path, int i) {
        if (i == maxPaliRoot) {
            paliRoots.add(new String(path) + (oddPali == 0 ? "" : oddPali) + new StringBuffer(new String(path)).reverse());
        } else if (i > maxPaliRoot) {
            return ;
        }
        
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            if (e.getValue() == 0) continue;
            mapCharToFreq.put(e.getKey(), e.getValue()-1);
            path[i] = e.getKey();
            buildPaliRoot(mapCharToFreq, path, i+1);
            mapCharToFreq.put(e.getKey(), e.getValue()+1);
            
        }
        
    }
    
    
    public Map buildMapCharToFreq(String s) {
        HashMap<Character, Integer> mapCharToFreq = new HashMap<>();
        for (char c: s.toCharArray()) {
            mapCharToFreq.put(c, mapCharToFreq.getOrDefault(c, 0)+1);
        };
        
        return mapCharToFreq;
    }
    
    public boolean isValidPali(Map<Character, Integer> mapCharToFreq) {
        int countOddFreq = 0;
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            if (e.getValue()%2==1) {
                countOddFreq++;
            }
        }
        
        return countOddFreq <= 1;
        
    }
}