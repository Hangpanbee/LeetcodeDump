class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        
        Deque<Integer> s = new ArrayDeque<>();
        
        for (int a: asteroids) {
            // a = -2
            // a = -1
            // a = 1
            // a = -2
            if (s.isEmpty() || s.peekLast() < 0 && a > 0 || s.peekLast()*a > 0 ) {
                s.offerLast(a);
                // s = [-2, -1, 1]
            } else {
                while (!s.isEmpty() && s.peekLast()*a < 0 && Math.abs(s.peekLast()) < Math.abs(a)) {
                    s.pollLast();
                }
                // at this state, aster stak only has abs value that is smaller than a or empty
                if (s.isEmpty()) {
                    s.offerLast(a);
                } else if (s.peekLast()*a > 0) {
                    // same direction
                    s.offerLast(a);
                } else if (s.peekLast() < 0 && a > 0) {
                    // opposite (l, r) but doesn't meet direction
                    s.offerLast(a);
                } else if (s.peekLast() == a*(-1)) {
                    // opposite (r, l) but does meet
                    s.pollLast();
                }
                
                
            }
        }
        int[] ans = new int[s.size()];
        for (int t = 0; t < ans.length; t++) {
            ans[t] = s.pollFirst();
        }
        
        return ans;
    }
}