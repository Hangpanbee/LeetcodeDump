class Solution {
    public long appealSum(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        long ans = 0;
        int prevState = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i))) {
                prevState = prevState+i+1;
                map.put(s.charAt(i), i);
                ans += prevState;
            } else {
                prevState = prevState + (i-map.get(s.charAt(i))-1) + 1;
                map.put(s.charAt(i), i);
                ans += prevState;
            };
            //System.out.println(prevState);
            //System.out.println(ans);
            
        };
        
        return ans;
        
    }
}