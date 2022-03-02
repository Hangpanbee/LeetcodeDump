class Solution {
    public boolean isSubsequence(String s, String t) {
        int s_i = 0;
        int t_i = 0;
        while (t_i < t.length() & s_i < s.length()) {
            if (s.charAt(s_i) == (t.charAt(t_i)) ) {
                s_i++;
                t_i++;
            } else {
                t_i++;
            };
        };
        
        return s_i == s.length() ? true : false;
        
    }
}