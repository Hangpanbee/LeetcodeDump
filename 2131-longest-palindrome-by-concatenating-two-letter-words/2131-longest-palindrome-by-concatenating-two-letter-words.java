class Solution {
    public int longestPalindrome(String[] words) {
        HashMap<String, Integer> mapWordToFreq = new HashMap<>();
        int ans = 0;
        for (String word: words) {
            String reversedWord = new StringBuilder(word).reverse().toString();
            if (mapWordToFreq.containsKey(reversedWord)) {
                ans += 4;
                mapWordToFreq.put(reversedWord, mapWordToFreq.get(reversedWord)-1);
                if (mapWordToFreq.get(reversedWord)==0) {
                    mapWordToFreq.remove(reversedWord);
                };
            } else {
                mapWordToFreq.put(word, mapWordToFreq.getOrDefault(word, 0)+1);
            }
            
        }
        
        // edge cases
        for (Map.Entry<String, Integer> m: mapWordToFreq.entrySet()) {
            String currS = m.getKey();
            if (currS.charAt(0) == currS.charAt(1)) {
                ans+=2;
                break;
            }
        }
        
        return ans;
        
        
    }
    

}