class Solution {
    public int calculate(String s) {
        
        Stack<Integer> st = new Stack<>();
        char opr = '+';
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                num = num*10 + (c - '0');
            } 
            if (c == '*' || c == '/' || c == '-' || c == '+' || i == (s.length()-1)) {
                if (opr == '-') st.add(-1*num);
                else if (opr == '+') st.add(num);
                else if (opr == '*') st.add(st.pop()*num);
                else if (opr == '/') st.add(st.pop()/num);
                // -> st = [3,2], opr = + 
                // -> st = [3,4] opr = *
                opr = c;
                num = 0;
            
            };    
        };
        
        int ans = 0;
        while (!st.empty()) {
            ans += st.pop();
        };
        
        return ans;
        
    }
    
}