class Solution {
    public String simplifyPath(String path) {
        String[] splittedPath = path.split("/");
        Stack<String> stack = new Stack<>();
        
        for (String s: splittedPath) {
            
            if (s.equals("") || s.equals(".") ) {
                continue;
            } else if (s.equals("..")) {
                if (stack.size() > 0) {
                    stack.pop();
                };
            } else {
                stack.push(s);
            };
            
        };
        
        if (stack.isEmpty()) return "/";
        
        StringBuilder ans = new StringBuilder("");
        for (String s: stack) {
            ans.append('/');
            ans.append(s);
            
        };
        
        return ans.toString();
        
    }
}