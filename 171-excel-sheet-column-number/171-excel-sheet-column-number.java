class Solution {
    public int titleToNumber(String columnTitle) {
        int ans = 0;
        int mult = columnTitle.length()-1;
        for (int i = 0; i < columnTitle.length(); i++) {
            char c = columnTitle.charAt(i);
            ans += ((int) c)%64*Math.pow(26, mult);
            mult--;
        };
        
        
        return ans;
    }
}