class Solution {
    public int calculate(String s) {
        
        Stack<Integer> st = new Stack<>();
        int num = 0;
        char opr = '+';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // -> c = '-'
            if (Character.isDigit(c)) {
                num = num*10 + c - '0';
            }
            if (c == '+' || c == '-' || c == '(' || c == ')' || i == (s.length()-1)) {
                if (opr == '+') st.add(num);
                else if (opr == '-') st.add(-1*num);
              
                
                if (c == ')') {
                int nxtNum = 0;    
                while (st.peek() != Integer.MAX_VALUE && st.peek() != Integer.MIN_VALUE) {
                    nxtNum += st.pop();
                };
                int sign = st.pop();
                sign = sign == Integer.MIN_VALUE ? -1 : 1;
                st.add(nxtNum*sign);
            
                } else if (c == '(') {
                    if (opr == '+') {
                        st.add(Integer.MAX_VALUE);
                    } else if (opr == '-') {
                        st.add(Integer.MIN_VALUE);
                        opr = '+';
                    }
                    // -> st = [-999999]
                }
                
        
                num = 0;
                if ((c == '+' || c == '-')) opr = c;
                
                
            }
            
            
            
        };
        int ans = 0;
        while (!st.isEmpty()) {
            ans += st.pop();
        };
        
        return ans;
        
        
        
    }
}