class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> tracker = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            
            int currTarget = target - nums[i];
            
            if (tracker.containsKey(currTarget)) {
                int left = tracker.get(currTarget);
                return new int[] {left, i};                
            } else {
                tracker.put(nums[i], i);
            }
        }
        

        return new int[2];
    }
}