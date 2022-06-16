class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        
        Stack<Integer> s = new Stack<>();
        
        for (int a: asteroids) {
            // a = -2
            // a = -1
            // a = 1
            // a = -2
            if (s.isEmpty() || s.peek() < 0 && a > 0 || s.peek()*a > 0 ) {
                s.add(a);
                // s = [-2, -1, 1]
            } else {
                while (!s.isEmpty() && s.peek()*a < 0 && Math.abs(s.peek()) < Math.abs(a)) {
                    s.pop();
                }
                // at this state, aster stak only has abs value that is smaller than a or empty
                if (s.isEmpty()) {
                    s.add(a);
                } else if (s.peek()*a > 0) {
                    // same direction
                    s.add(a);
                } else if (s.peek() < 0 && a > 0) {
                    // opposite (l, r) but doesn't meet direction
                    s.add(a);
                } else if (s.peek() == a*(-1)) {
                    // opposite (r, l) but does meet
                    s.pop();
                }
                
                
            }
            
        
        }
        
        int[] ans = new int[s.size()];
        for (int t = ans.length-1; t >= 0; t--) {
            ans[t] = s.pop();
        }
        
        return ans;
    }
}