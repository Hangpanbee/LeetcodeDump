class Solution {
    int maxPaliRoot;
    List<String> paliRoots;
    public List<String> generatePalindromes(String s) {
        Map<Character, Integer> mapCharToFreq = buildMapCharToFreq(s);
        if (!isValidPali(mapCharToFreq)) return new ArrayList<>();
        
        maxPaliRoot = s.length()/2;
        paliRoots = new ArrayList<String>();
        char oddPali = 0;
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            if (e.getValue()%2==1) {
                oddPali = e.getKey();
                mapCharToFreq.put(e.getKey(), (e.getValue()-1)/2);
            } else {
                mapCharToFreq.put(e.getKey(), e.getValue()/2);
            }
        }
        
        buildPaliRoot(mapCharToFreq, new StringBuilder());
        //System.out.println(oddPali);
        List<String> paliPerm = new ArrayList<>();
        for (String paliRoot: paliRoots) {
            paliPerm.add(new String(paliRoot) + (oddPali == 0 ? "" : oddPali) + new StringBuffer(new String(paliRoot)).reverse());
        }
        
        return paliPerm;
        
        
        
    }
    
    public void buildPaliRoot(Map<Character, Integer> mapCharToFreq, StringBuilder path) {
        if (path.length() == maxPaliRoot) {
            paliRoots.add(path.toString());
        } else if (path.length() > maxPaliRoot) {
            return ;
        }
        
        for (Map.Entry<Character, Integer> e: mapCharToFreq.entrySet()) {
            if (e.getValue() == 0) continue;
            mapCharToFreq.put(e.getKey(), e.getValue()-1);
            buildPaliRoot(mapCharToFreq, path.append(e.getKey()));
            path.delete(path.length()-1, path.length());
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