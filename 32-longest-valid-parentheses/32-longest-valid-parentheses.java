class Solution {
    public int longestValidParentheses(String s1) {
        Stack<Integer> st = new Stack<>();
        char[] s = s1.toCharArray();
        int[] dp = new int[s.length+1];
        int ans = 0;
        for (int i = 0; i < s.length; i++) {
            if (s[i] == '(') {
                st.add(i);
            } else {
                if (st.size() > 0) {
                    int poppedI = st.pop();
                    int nxtState = st.size() > 0 ? st.peek() : -1;
                    dp[nxtState+1] += dp[poppedI+1]+2;
                    ans = Math.max(ans, dp[nxtState+1]);
                    
                } else {
                    dp[0] = 0;
                }
            };
            
        };
        //System.out.println(Arrays.toString(dp));
        return Math.max(ans, dp[0]);
        
        
    }
}