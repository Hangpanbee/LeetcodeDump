class Solution {
    public boolean canPermutePalindrome(String s) {
        // if all char but one is odd then true || all char%2==0
        
        Map<Character, Integer> mapCharToFreq = new HashMap<>();
        
        for (char c: s.toCharArray()) {
            mapCharToFreq.put(c, mapCharToFreq.getOrDefault(c, 0) + 1);
        };
        
        int countOddChar = 0;
        for (Map.Entry<Character, Integer> m: mapCharToFreq.entrySet()) {
            if (m.getValue()%2==1) {
                countOddChar++;
            };
        };
        
        return countOddChar <= 1;
        
        
    }
}