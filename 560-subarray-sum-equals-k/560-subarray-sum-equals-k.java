class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap <Integer, Integer> sum_tracker = new HashMap<Integer, Integer>();
        
        int running_sum = 0;
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            running_sum += nums[i];
            
            if (sum_tracker.containsKey(running_sum - k)) {
                ans += sum_tracker.get(running_sum-k);
            } 
            
            if (running_sum == k) {
                ans += 1;
            }
            
            
            
            
            if (sum_tracker.containsKey(running_sum)) {
                sum_tracker.put(running_sum, sum_tracker.get(running_sum) + 1);
                
            } else {
                sum_tracker.put(running_sum, 1);
            };
        };
        return ans;    
        
    }
}