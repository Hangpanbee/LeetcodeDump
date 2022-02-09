class Solution {
    public int findPairs(int[] nums, int k) {
        HashMap<Integer, Integer> prev_num_tracker = new HashMap<Integer, Integer>();
        Set<Pair> ans = new HashSet<Pair>();
        
        for (int i = 0; i < nums.length; i++) {
            int lower_target = k + nums[i];
            int upper_target = nums[i] - k;
            
            if (prev_num_tracker.containsKey(lower_target)) {
                if (lower_target > nums[i]) {
                    ans.add(new Pair(nums[i], lower_target));
                } else {
                    ans.add(new Pair(lower_target, nums[i]));
                }
            }
            if (prev_num_tracker.containsKey(upper_target)) {
                if (upper_target > nums[i]) {
                    ans.add(new Pair(nums[i], upper_target));
                } else {
                    ans.add(new Pair(upper_target, nums[i]));
                }
            }
            
            prev_num_tracker.put(nums[i], 1);
        }
        
        return ans.size();
        
    }
}