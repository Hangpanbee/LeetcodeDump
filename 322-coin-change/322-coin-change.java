class Solution {
    int[] coins;
    Map<Integer, Integer> memoize;
    public int coinChange(int[] _coins, int amount) {
        memoize = new HashMap<>();
        int ans = helper(_coins, amount);
        return ans > 9999999 ? -1 : ans;
    }
    
    public int helper(int[] coins, int amount) {
        if (amount < 0) {
            return 9999999;
        } else if (amount == 0) {
            return 0;
        } else if (memoize.containsKey(amount)) {
            return memoize.get(amount);
        }
        
        
        int min = Integer.MAX_VALUE;
        for (int coin: coins) {
            int currCoinCount = 1 + helper(coins, amount - coin);
            min = Math.min(currCoinCount, min);
        };
        memoize.put(amount, min);
        return min;
        
        
        
    }
    
    
    
}